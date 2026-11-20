# 服务变化提示与复核工作台：资料说明

用于筛选可能需要人工复核的服务变化，并记录复核处置。合成数据不代表真实网格绩效。

每个 JSON 文件均为 UTF-8 编码。空字符串表示来源没有给出该事实，不等同于零、否或业务终态。标识仅在本项目资料内有意义。

## `observations.json`

字段：grid, month, category, eligible, received, timely, matured, revision。共 5 条合成记录。

## `context.json`

字段：grid, month, kind, value。共 3 条合成记录。

## `reviews.json`

字段：id, grid, period, signal_key, status, reason。共 3 条合成记录。

## `definitions.json`

字段：id, signal, version, minimum_matured, lookback_months。共 2 条合成记录。

## 关系与口径提示

observations 按网格、月份和类别汇总；matured 是已有充分结果的事项数。context 记录同期间可能影响解释的变化；reviews.signal_key 用于关联待复核信号，状态是人工决定，不是源数据。
