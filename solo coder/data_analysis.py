import csv
import os

def read_csv_file(file_path):
    if not os.path.exists(file_path):
        print(f"错误：文件 {file_path} 不存在！")
        return None
    
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    
    return data

def convert_to_numeric(data):
    numeric_data = []
    for row in data:
        numeric_row = {}
        for key, value in row.items():
            try:
                numeric_row[key] = float(value) if '.' in value else int(value)
            except ValueError:
                numeric_row[key] = value
        numeric_data.append(numeric_row)
    return numeric_data

def calculate_statistics(data, columns):
    stats = {}
    for col in columns:
        values = [row[col] for row in data]
        stats[col] = {
            '平均值': round(sum(values) / len(values), 2),
            '最大值': max(values),
            '最小值': min(values),
            '总和': sum(values)
        }
    return stats

def sort_by_column(data, column, ascending=True):
    return sorted(data, key=lambda x: x[column], reverse=not ascending)

def print_statistics(stats):
    print("\n" + "="*60)
    print("基础统计分析结果")
    print("="*60)
    
    for col, col_stats in stats.items():
        print(f"\n【{col}】")
        print(f"  平均值: {col_stats['平均值']}")
        print(f"  最大值: {col_stats['最大值']}")
        print(f"  最小值: {col_stats['最小值']}")
        print(f"  总和: {col_stats['总和']}")

def print_sorted_data(data, sort_column, ascending=True):
    order = "升序" if ascending else "降序"
    print("\n" + "="*60)
    print(f"按【{sort_column}】{order}排序结果")
    print("="*60)
    
    if not data:
        print("没有数据可显示")
        return
    
    headers = list(data[0].keys())
    header_line = " | ".join(f"{h:^10}" for h in headers)
    print(header_line)
    print("-" * len(header_line))
    
    for row in data:
        row_line = " | ".join(f"{str(v):^10}" for v in row.values())
        print(row_line)

def main():
    csv_file = 'students.csv'
    
    print("="*60)
    print("学生成绩数据分析系统")
    print("="*60)
    
    data = read_csv_file(csv_file)
    if data is None:
        return
    
    print(f"\n成功读取 {len(data)} 条数据记录")
    
    numeric_data = convert_to_numeric(data)
    
    numeric_columns = ['年龄', '数学', '语文', '英语', '总分']
    
    stats = calculate_statistics(numeric_data, numeric_columns)
    print_statistics(stats)
    
    sorted_by_total = sort_by_column(numeric_data, '总分', ascending=False)
    print_sorted_data(sorted_by_total, '总分', ascending=False)
    
    sorted_by_math = sort_by_column(numeric_data, '数学', ascending=False)
    print_sorted_data(sorted_by_math, '数学', ascending=False)
    
    print("\n" + "="*60)
    print("数据分析完成！")
    print("="*60)

if __name__ == "__main__":
    main()
