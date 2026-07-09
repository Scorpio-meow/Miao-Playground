# 愛情進行時 (Love in Progress)

![Language](https://img.shields.io/badge/Language-Python%203-blue)
![GUI](https://img.shields.io/badge/GUI-Tkinter-yellowgreen)
![Platform](https://img.shields.io/badge/Platform-Windows%20%2F%20macOS%20%2F%20Linux-orange)
![License](https://img.shields.io/badge/License-MIT-green)

愛情進行時 (Love in Progress) 是一個基於 Python Tkinter 開發的趣味彈窗動畫程式。它會在螢幕上以數學心形曲線軌跡動態繪製多個置頂的溫馨提示視窗，隨後在螢幕隨機位置鋪滿祝福彈窗，並在指定時間後以動畫形式快速依序銷毀所有視窗。這是一個適合用於告白、節日驚喜或個人溫馨提醒的趣味小工具。

---

## 快速開始

### 系統要求

- 已安裝 Python 3.x 環境。
- 已安裝 Tkinter 元件。
  - **Windows**：多數 Python 安裝程式已預設內建。
  - **macOS**：若透過 Homebrew 安裝 Python，通常已內建。若未內建，可執行 `brew install python-tk`。
  - **Linux**（例如 Ubuntu/Debian）：若未安裝，請在終端機中執行：
    ```bash
    sudo apt-get install python3-tk
    ```

### 執行步驟

請在終端機中執行以下命令來啟動程式：

```bash
python Love-in-Progress.py
```

### 操作與安全機制

> [!IMPORTANT]
> **安全退出鍵**：在程式執行期間，任何時候按下 **空白鍵 (Space)** 即可立即關閉所有已生成的彈窗並安全結束程式。此機制旨在防止彈窗干擾您的正常電腦操作。

---

## 功能特點

- **心形軌跡繪製**：利用心形數學公式計算出 100 個螢幕座標點，依序動態生成彈窗，在螢幕中央拼出一個愛心形狀。
- **隨機祝福彈窗**：心形彈窗消失後，會在螢幕隨機位置快速生成鋪滿螢幕的隨機祝福語彈窗。
- **自動銷毀動畫**：所有隨機彈窗在顯示 10 秒後，會以極快的速度依序銷毀，呈現收縮消失的視覺效果。
- **隨機祝福語與顏色**：每次生成的彈窗會隨機從預設的溫馨詞庫與粉嫩色系庫中挑選。
- **安全退出機制**：任何時候按下空白鍵即可瞬間關閉所有產生的視窗並結束程式。

---

## 自訂配置

您可以直接編輯 [Love-in-Progress.py](./Love-in-Progress.py) 中的變數來進行個人化配置：

| 變數或函數 | 說明 | 預設值 |
| :--- | :--- | :--- |
| `t` | 彈窗顯示的祝福語列表 | `["愛你老幾", "好好愛自己", "好好吃飯", "保持好心情", "我想你了", "順順利利", "別熬夜", "天涼了多穿衣服"]` |
| `c` | 彈窗背景顏色列表 | `["pink", "lightblue", "lightgreen", "lemonchiffon", "hotpink", "skyblue"]` |
| `n` | 心形軌跡的彈窗數量 | `100` |
| `wx` 函數中的字型 | 彈窗文字的字型與大小 | `("Microsoft YaHei", 14)` |
| `wx` 函數中的尺寸 | 每個彈窗的寬度與高度 | `150x60` |

---

## 程式碼架構

本專案主要由單一檔案 [Love-in-Progress.py](./Love-in-Progress.py) 組成。核心函式如下：

- **`g(n, w, h)`**：心形曲線座標生成函數。使用經典的愛心曲線公式計算出 `n` 個點的座標，並將其映射至螢幕中央區域。
- **`wx(x, y, tip=None, is_h=True)`**：建立置頂的 `tk.Toplevel` 提示視窗，並為其綁定空白鍵退出事件。
- **`w()`**：主控制流程。負責初始化視窗環境、動態生成心形軌跡彈窗、延時銷毀、生成鋪滿螢幕的隨機彈窗，以及最後的依序淡出銷毀動畫。

---

## 授權條款

本專案採用 [MIT License](./LICENSE) 授權釋出。