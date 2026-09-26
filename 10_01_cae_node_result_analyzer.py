"""CAE 节点结果分析器示例。

功能：
1. 读取节点位移与应力结果；
2. 计算位移合量和 von Mises 等效应力；
3. 根据许用应力计算安全系数并判断是否超限；
4. 输出汇总信息，并把逐节点结果保存为 CSV。

不指定输入文件时，程序使用内置示例数据，因此可以直接运行。
"""

import argparse
import csv
import math
from pathlib import Path


# 输入 CSV 必须包含这些列。位移和应力的单位应当在整个文件中保持一致。
REQUIRED_FIELDS = (
    "node_id",
    "x",
    "y",
    "z",
    "ux",
    "uy",
    "uz",
    "sxx",
    "syy",
    "szz",
    "sxy",
    "syz",
    "szx",
)


# 直接运行脚本时使用的示例数据。
SAMPLE_NODES = [
    {
        "node_id": 1,
        "x": 0.0,
        "y": 0.0,
        "z": 0.0,
        "ux": 0.10,
        "uy": 0.00,
        "uz": 0.00,
        "sxx": 100.0,
        "syy": 50.0,
        "szz": 20.0,
        "sxy": 10.0,
        "syz": 0.0,
        "szx": 0.0,
    },
    {
        "node_id": 2,
        "x": 10.0,
        "y": 0.0,
        "z": 0.0,
        "ux": 0.20,
        "uy": 0.05,
        "uz": 0.00,
        "sxx": 180.0,
        "syy": 80.0,
        "szz": 40.0,
        "sxy": 25.0,
        "syz": 5.0,
        "szx": 0.0,
    },
    {
        "node_id": 3,
        "x": 20.0,
        "y": 0.0,
        "z": 0.0,
        "ux": 0.35,
        "uy": 0.10,
        "uz": 0.05,
        "sxx": 320.0,
        "syy": 90.0,
        "szz": 60.0,
        "sxy": 35.0,
        "syz": 10.0,
        "szx": 8.0,
    },
    {
        "node_id": 4,
        "x": 30.0,
        "y": 0.0,
        "z": 0.0,
        "ux": 0.15,
        "uy": 0.03,
        "uz": 0.02,
        "sxx": 130.0,
        "syy": 65.0,
        "szz": 30.0,
        "sxy": 18.0,
        "syz": 3.0,
        "szx": 2.0,
    },
]


def calculate_displacement_magnitude(ux, uy, uz):
    """计算位移合量：sqrt(ux^2 + uy^2 + uz^2)。"""
    return math.sqrt(ux**2 + uy**2 + uz**2)


def calculate_von_mises(sxx, syy, szz, sxy, syz, szx):
    """根据三维应力分量计算 von Mises 等效应力。"""
    normal_part = 0.5 * (
        (sxx - syy) ** 2 + (syy - szz) ** 2 + (szz - sxx) ** 2
    )
    shear_part = 3.0 * (sxy**2 + syz**2 + szx**2)
    return math.sqrt(normal_part + shear_part)


def read_nodes_from_csv(input_path):
    """从 CSV 读取节点数据，并将数值文本转换为 int 或 float。"""
    nodes = []

    with input_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        actual_fields = set(reader.fieldnames or [])
        missing_fields = set(REQUIRED_FIELDS) - actual_fields

        if missing_fields:
            missing_text = ", ".join(sorted(missing_fields))
            raise ValueError(f"输入 CSV 缺少字段：{missing_text}")

        for line_number, row in enumerate(reader, start=2):
            try:
                node = {"node_id": int(row["node_id"])}
                for field in REQUIRED_FIELDS[1:]:
                    node[field] = float(row[field])
            except (TypeError, ValueError) as error:
                raise ValueError(f"第 {line_number} 行包含无效数值") from error

            nodes.append(node)

    if not nodes:
        raise ValueError("输入 CSV 没有节点数据")

    return nodes


def analyze_nodes(nodes, allowable_stress):
    """计算每个节点的派生结果，并返回新的结果列表。"""
    results = []

    for node in nodes:
        displacement = calculate_displacement_magnitude(
            node["ux"], node["uy"], node["uz"]
        )
        von_mises = calculate_von_mises(
            node["sxx"],
            node["syy"],
            node["szz"],
            node["sxy"],
            node["syz"],
            node["szx"],
        )

        # 应力为 0 时不存在除零问题，安全系数记为无穷大。
        safety_factor = math.inf if von_mises == 0 else allowable_stress / von_mises

        result = node.copy()
        result["displacement_magnitude"] = displacement
        result["von_mises"] = von_mises
        result["safety_factor"] = safety_factor
        result["status"] = "超限" if von_mises > allowable_stress else "合格"
        results.append(result)

    return results


def print_summary(results, allowable_stress):
    """在终端打印整体分析摘要。"""
    max_displacement_node = max(results, key=lambda item: item["displacement_magnitude"])
    max_stress_node = max(results, key=lambda item: item["von_mises"])
    failed_nodes = [item for item in results if item["status"] == "超限"]

    print("\nCAE 节点结果分析摘要")
    print(f"节点数量：{len(results)}")
    print(f"许用应力：{allowable_stress:.3f}")
    print(
        "最大位移："
        f"{max_displacement_node['displacement_magnitude']:.6f}，"
        f"节点 {max_displacement_node['node_id']}"
    )
    print(
        "最大 von Mises 应力："
        f"{max_stress_node['von_mises']:.3f}，"
        f"节点 {max_stress_node['node_id']}"
    )
    print(f"超限节点数量：{len(failed_nodes)}")

    if failed_nodes:
        failed_ids = ", ".join(str(item["node_id"]) for item in failed_nodes)
        print(f"超限节点：{failed_ids}")
    else:
        print("所有节点均未超过许用应力。")


def write_results_to_csv(results, output_path):
    """将原始数据和分析结果写入新的 CSV。"""
    output_fields = list(REQUIRED_FIELDS) + [
        "displacement_magnitude",
        "von_mises",
        "safety_factor",
        "status",
    ]

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=output_fields)
        writer.writeheader()
        writer.writerows(results)


def parse_arguments():
    """读取命令行参数。"""
    parser = argparse.ArgumentParser(description="分析 CAE 节点位移与应力结果")
    parser.add_argument(
        "--input",
        type=Path,
        help="输入 CSV 路径；省略时使用脚本内置的示例数据",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("cae_node_analysis_results.csv"),
        help="输出 CSV 路径",
    )
    parser.add_argument(
        "--allowable-stress",
        type=float,
        default=235.0,
        help="许用应力，默认值为 235.0；单位应与输入应力一致",
    )
    return parser.parse_args()


def main():
    """组织数据读取、计算、打印和导出流程。"""
    args = parse_arguments()

    if args.allowable_stress <= 0:
        raise ValueError("许用应力必须大于 0")

    if args.input is None:
        nodes = SAMPLE_NODES
        print("未指定输入文件，正在使用内置示例数据。")
    else:
        nodes = read_nodes_from_csv(args.input)
        print(f"已读取输入文件：{args.input}")

    results = analyze_nodes(nodes, args.allowable_stress)
    print_summary(results, args.allowable_stress)
    write_results_to_csv(results, args.output)
    print(f"分析结果已保存至：{args.output.resolve()}")


if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, PermissionError, ValueError) as error:
        print(f"分析失败：{error}")
