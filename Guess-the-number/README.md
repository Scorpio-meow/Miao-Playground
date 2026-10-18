# 猜數字遊戲 (Guess the Number)

![Language](https://img.shields.io/badge/Language-HTML5%20%2F%20CSS3%20%2F%20JavaScript-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Web%20Browser-orange)

一個基於 HTML5、CSS3 與 JavaScript (ES6) 網頁技術開發的單機版經典猜數字小遊戲。玩家需要在 1 到 100 的範圍內猜測系統隨機生成的秘密數字，系統會根據玩家輸入的數值即時給予高低提示。本專案專注於極簡的程式碼結構與直覺的操作體驗。

---

## 快速開始

本專案為純前端網頁應用，無任何外部相依套件，亦不需進行編譯，即可在各種現代瀏覽器中流暢運行。

### 方式一：直接點擊運行

1. 下載或複製本專案的程式碼。
2. 在檔案瀏覽器中找到 [index.html](./index.html)。
3. 雙擊該檔案，即可直接以預設瀏覽器開啟並開始遊玩。

### 方式二：使用本地開發伺服器（推薦）

若您希望透過本地網頁伺服器（Local Server）開啟，可以使用 Bun 來啟動靜態伺服器以獲得更好的瀏覽器安全上下文與載入體驗：

1. 確保您的系統已安裝 Bun 執行環境。
2. 在專案根目錄下執行以下指令安裝並開啟靜態伺服器：
   ```bash
   bunx serve .
   ```
3. 開啟瀏覽器並造訪 `http://localhost:3000`（或終端機輸出的對應埠號）。

---

## 遊戲功能與設計細節

- **隨機秘密數字生成**：每次重新載入頁面時，系統會自動生成一個介於 1 至 100 之間的隨機整數作為答案。
- **即時回饋提示**：
  - **數值過高**：當猜測值大於秘密數字時，顯示紅色提示文字 `Too high!`。
  - **數值過低**：當猜測值小於秘密數字時，顯示橘色提示文字 `Too low!`。
  - **猜中答案**：當猜測值等於秘密數字時，顯示綠色提示文字 `Congratulations! You guessed it!`。
- **防呆輸入驗證**：若輸入非數字、小於 1 或大於 100 的無效數值，系統會即時提醒「Please enter a number between 1 and 100.」，此操作不會被視為無效猜測。

---

## 專案結構

本專案採用單一檔案架構，便於學習、部署與快速修改：

* [index.html](./index.html)：包含遊戲的 HTML5 結構、CSS3 樣式定義，以及核心 JavaScript 遊戲邏輯。

---

## 自訂配置與開發指南

### 自訂數字範圍

若您希望自訂遊戲的規則（例如修改數字範圍），可直接編輯 [index.html](./index.html) 的內容：

> [!NOTE]
> 修改範圍時，請務必同步更新 HTML 提示文字與 `<input>` 的限制屬性，以確保 UI 提示與實際邏輯相符。

| 配置項目 | 程式碼相關位置 | 預設值 | 修改說明 |
| :--- | :--- | :--- | :--- |
| **數字下限** | `min="1"`, `guess < 1`, `+ 1` | 1 | 調整隨機數生成偏移量及防呆判斷值。 |
| **數字上限** | `max="100"`, `guess > 100`, `* 100` | 100 | 調整 `Math.random()` 相乘基數及輸入最大值限制。 |

#### 修改範例（將範圍調整為 1 至 500）：
在 [index.html](file:///d:/Code/Guess-the-number/index.html) 中進行以下修改：
```html
<!-- 修改輸入框屬性與提示標籤 -->
<label for="guessInput">Guess a number between 1 and 500:</label>
<input type="number" id="guessInput" min="1" max="500" placeholder="1-500">
```
```javascript
// 修改 JavaScript 隨機數生成與防呆邊界
let secretNumber = Math.floor(Math.random() * 500) + 1;
if (isNaN(guess) || guess < 1 || guess > 500) {
    message.textContent = "Please enter a number between 1 and 500.";
    return;
}
```

---

## 未來展望與貢獻指南

歡迎提交 Issue 或 Pull Request 來共同改進此遊戲。以下是一些可供擴充的開發方向：
1. **歷史紀錄功能**：新增猜測次數計數器，以及過去猜測數字的歷史紀錄列表。
2. **難易度選擇**：新增難度選單，支援簡單（1-50）、中等（1-100）及困難（1-1000）模式。
3. **介面視覺美化**：導入現代 CSS 框架或加入更具動感的 UI 與過渡動畫。

---

## 授權條款

本專案採用 [MIT License](./LICENSE) 授權條款釋出。
