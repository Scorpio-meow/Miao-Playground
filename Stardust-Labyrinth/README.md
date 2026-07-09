# 星塵迷宮 (Stardust Labyrinth)

![Language](https://img.shields.io/badge/Language-Python%203-blue)
![Platform](https://img.shields.io/badge/Platform-Terminal%20%2F%20Console-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

星塵迷宮是一款基於 Python 終端機開發的純文字迷宮冒險小遊戲。玩家需要在躲避幽靈追擊的同時，收集迷宮中散落的所有星塵。本專案以極簡的代碼實現了經典的 2D 格子地圖渲染、基於曼哈頓距離的尋路追擊演算法，以及終端機互動控制。

---

## 快速開始

### 系統要求

- Python 3.7 或更高版本。

### 執行遊戲

此遊戲不需要安裝任何第三方套件，直接使用 Python 內建標準函式庫即可運行。

請在終端機中執行以下指令：

```bash
python "Stardust Labyrinth.py"
```

---

## 遊戲規則與控制

### 地圖元件說明

| 符號 | 名稱 | 角色與功能說明 |
| :---: | :--- | :--- |
| **`@`** | **玩家** | 您控制的角色，目標是收集完所有星塵。 |
| **`*`** | **星塵** | 散落在迷宮中的能量，收集完地圖上所有的星塵即可獲勝。 |
| **`G`** | **幽靈** | 追逐玩家的敵人。每回合會往最靠近玩家的方向移動一步。 |
| **`#`** | **牆壁** | 無法穿過的實體障礙物。 |
| **`.`** | **通道** | 玩家與幽靈可以自由移動的空白路徑。 |

### 控制方式

在遊戲提示輸入時，輸入以下單一字元並按下 Enter 鍵：

- `w`：向上移動一步。
- `a`：向左移動一步。
- `s`：向下移動一步。
- `d`：向右移動一步。
- `q`：結束遊戲並退出。

---

## 幽靈追擊演算法

幽靈每回合會嘗試尋找與玩家之間曼哈頓距離（Manhattan Distance）最小的相鄰通道，並向該方向移動一步。計算方式如下：

$$\text{Distance} = |r_{\text{ghost}} - r_{\text{player}}| + |c_{\text{ghost}} - c_{\text{player}}|$$

其中 $(r, c)$ 分別代表角色在二維地圖中的列（Row）與行（Column）索引。

在每一回合更新時，系統會計算幽靈周圍四個方向的可行通道，並依據距離大小進行排序，優先選擇能夠縮短距離的格子：

```python
# 核心追擊演算法邏輯
candidates = []
for dr, dc in DIRS.values():
    nr, nc = gr + dr, gc + dc
    if self.board[nr][nc] != '#':
        dist = abs(pr - nr) + abs(pc - nc)
        candidates.append((dist, nr, nc))
# 排序：距離優先，其次是列號，再次是行號
candidates.sort(key=lambda x: (x[0], x[1], x[2]))
_, nr, nc = candidates[0]
self.ghost = (nr, nc)
```

---

## 自訂配置

您可以透過修改 [Stardust Labyrinth.py](./Stardust%20Labyrinth.py) 檔案中的 `RAW_MAP` 陣列來自行設計專屬的迷宮地圖。

### 預設地圖定義

```python
RAW_MAP = [
    '###########',
    '#@..#....*#',
    '#.#.#.##..#',
    '#.#...#...#',
    '#.###.#.#.#',
    '#...#...#.#',
    '#.#.###.#.#',
    '#.#...#...#',
    '#..##.#.#G#',
    '#*....#..*#',
    '###########',
]
```

### 地圖編輯規範

> [!WARNING]
> 設計自訂地圖時，請確保：
> 1. 地圖的邊界應被牆壁 `#` 包圍，以防止玩家或幽靈移出界外。
> 2. 地圖中必須且只能有一個玩家起點 `@` 與一個幽靈起點 `G`。
> 3. 地圖中應至少包含一個星塵 `*`。

---

## 程式碼架構

本專案所有核心邏輯皆封裝於單一檔案 [Stardust Labyrinth.py](./Stardust%20Labyrinth.py) 中：

- [Game 類別](./Stardust%20Labyrinth.py#L37-L42)：核心遊戲狀態管理類別。
  - `from_map`：分析字元矩陣並初始化遊戲狀態（包括玩家與幽靈座標、星塵位置集合等）。
  - `draw`：在終端機中清屏並重新繪製目前的迷宮地圖與狀態欄。
  - `step_player`：根據輸入更新玩家位置，進行牆壁碰撞偵測，並處理星塵收集邏輯。
  - `step_ghost`：執行幽靈尋路追擊。
  - `player_caught`：判定幽靈是否與玩家重合。
- [main 函數](./Stardust%20Labyrinth.py#L111-L150)：程式入口點，負責遊戲主迴圈、輸入處理以及勝負判斷。

---

## 授權條款

本專案採用 [MIT License](./LICENSE) 授權條款釋出。
