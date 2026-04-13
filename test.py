# 1. 获取仓库URL（在GitHub仓库页面点击"Code"→复制HTTPS链接）
git clone https://github.com/你的用户名/team-project-demo.git

# 2. 进入项目目录
cd team-project-demo

# 3. 查看当前状态
git status

# 4. 创建项目文件
echo "# 小组项目：学习记录系统" > README.md
echo "" >> README.md
echo "## 项目简介" >> README.md
echo "这是一个用于记录学习进度的协作项目。" >> README.md

# 5. 创建Python程序文件
cat > learning_tracker.py << 'EOF'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
学习记录系统主程序
作者：张三
创建日期：2024-01-15
"""

def display_menu():
    """显示菜单"""
    print("=== 学习记录系统 ===")
    print("1. 添加学习记录")
    print("2. 查看学习记录")
    print("3. 统计学习时间")
    print("4. 退出系统")

def add_record():
    """添加学习记录"""
    subject = input("请输入学习科目：")
    duration = input("请输入学习时长（小时）：")
    date = input("请输入日期（YYYY-MM-DD）：")
    
    with open("study_records.txt", "a") as f:
        f.write(f"{date},{subject},{duration}\n")
    print("学习记录添加成功！")

def main():
    """主函数"""
    while True:
        display_menu()
        choice = input("请选择操作（1-4）：")
        
        if choice == "1":
            add_record()
        elif choice == "2":
            print("功能开发中...")
        elif choice == "3":
            print("功能开发中...")
        elif choice == "4":
            print("感谢使用，再见！")
            break
        else:
            print("无效选择，请重新输入！")

if __name__ == "__main__":
    main()
EOF

# 6. 查看文件状态
git status

# 7. 将文件添加到暂存区
git add README.md learning_tracker.py

# 8. 查看暂存区状态
git status

# 9. 提交更改
git commit -m "初始提交：创建项目框架和主程序文件"

# 10. 查看提交历史
git log

# 11. 推送到远程仓库
git push origin main
