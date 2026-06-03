# SnailBox 发布构建手册

## 概述

SnailBox 使用自动化构建脚本，从开发版 (`SnailBox_dev`) 生成精简的发布版 (`SnailBox`)。构建过程包括文件筛选排除、源码编译为 PYD、以及发布目录清理。

## 文件说明

| 文件 | 用途 |
|------|------|
| `release_build.py` | 构建脚本，读取配置并执行构建 |
| `release_config.json` | 构建配置清单，定义排除/编译/保留规则 |
| `release_doc.md` | 本文档 |

## 使用方法

```bash
cd G:\SnailBox\SnailBox_dev
python release_build.py [config_path]
```

- 默认读取同目录下 `release_config.json`
- 可指定自定义配置文件路径作为参数

## 构建流程

### [1/4] 清理发布目录

删除发布目录中所有内容，**保留** `preserve_in_output` 列表中的文件/目录。

保留策略：
- 顶层项目（如 `.git`、`LICENSE`）直接保留
- 嵌套路径（如 `toolbar/snailBox.shelf`）保留其所在目录，仅清理非保留文件

### [2/4] 复制文件

从开发版目录复制文件到发布目录，自动跳过：

- `exclude_dirs` 中列出的整个目录
- `exclude_files` 中列出的具体文件
- `exclude_patterns` 中匹配的文件（通配符）
- `pyd_convert` 中的文件（这些会被编译为 PYD）
- `preserve_in_output` 中的文件（保留发布版自己的版本）

### [3/4] 编译 PYD

对 `pyd_convert` 列表中的 .py 文件：

1. 读取源码
2. 自动去除注释和返回类型注解（如 `-> str`）
3. 写入临时 .py 到发布目录
4. 调用 `easycython` 编译为 .pyd
5. 清理临时文件（.py、.c、.html、build/）

### [4/4] 清理缓存

删除发布目录下所有 `__pycache__/` 目录。

## 配置说明 (release_config.json)

```jsonc
{
  "source_dir": ".",                    // 开发版路径（相对于脚本所在目录）
  "output_dir": "G:\\SnailBox\\SnailBox",  // 发布版输出路径
  "pyd_versions": ["3.11"],             // 编译的 Python 版本列表

  "exclude_dirs": [],       // 排除的目录（整个目录不进入发布版）
  "exclude_files": [],      // 排除的具体文件
  "exclude_patterns": [],   // 排除的通配符模式
  "pyd_convert": [],        // 编译为 PYD 的 .py 文件
  "preserve_in_output": []  // 发布版中保留不覆盖的文件
}
```

## 注意事项

### PYD 编译兼容性

- **返回类型注解**：`-> str`、`-> int` 等 Cython 无法兼容，构建脚本会自动去除
- **Qt 类型注解**：如 `QtCore.QRect` 会产生警告但不影响编译
- **language_level**：Cython 默认使用 `3str`，会在日志中产生 FutureWarning，可忽略

### preserve_in_output 行为

- 保留文件在清理步骤**不会被删除**
- 保留文件在复制步骤**不会被覆盖**
- 支持嵌套路径（如 `toolbar/snailBox.shelf`）
- 发布版独有的文件（如 `LICENSE`）应加入此列表

### 日常维护

- **新增需要编译的文件**：在 `pyd_convert` 中添加路径
- **新增排除模块**：在 `exclude_dirs` 或 `exclude_files` 中添加
- **新增发布版独有文件**：在 `preserve_in_output` 中添加
- **支持多版本 Houdini**：修改 `pyd_versions`，如 `["3.9", "3.10", "3.11"]`

### 发布流程

构建完成后需手动操作：

```bash
cd G:\SnailBox\SnailBox
git status        # 检查变更
git add -A
git commit -m "版本号_描述"
git push
```

### 依赖

- Python 3.11（与编译目标版本一致）
- [easycython](https://pypi.org/project/easycython/)：`pip install easycython cython`
- easycython 需为对应版本：`pip install easycython`（在目标 Python 环境中）
