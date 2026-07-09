# 貓咪遊樂場 (Miao Playground)

歡迎來到貓咪遊樂場。本專案庫收錄了多個不同類型、使用不同技術開發的趣味小遊戲與互動小工具，旨在提供豐富的互動體驗與清晰的程式碼範例。

---

## 專案導覽

本遊樂場目前包含以下五個子專案，您可以點擊專案名稱進入其專屬的詳細說明文件：

| 專案名稱 | 執行環境 | 主要技術 | 簡介 | 詳細文件 |
| :--- | :--- | :--- | :--- | :--- |
| **液體解鎖 (Liquid Cipher)** | 網頁瀏覽器 | HTML5 Canvas / Web Audio API / Tailwind CSS | 模擬減法三原色（RYB）色素混色的試管液體分類解密遊戲，具備即時音效合成與無限制復原功能。 | [檢視說明](./Liquid-Cipher/README.md) |
| **星塵迷宮 (Stardust Labyrinth)** | 終端機 | Python 3 | 經典純文字迷宮冒險遊戲，幽靈會透過曼哈頓距離尋路追擊玩家，支援自訂地圖設計。 | [檢視說明](./Stardust-Labyrinth/README.md) |
| **量子猜拳 (Quantum Duel)** | 終端機 | Python 3 | 結合斬擊、格擋與蓄能機制的策略心理戰對戰遊戲，AI 會根據當前局勢動態調整決策權重。 | [檢視說明](./Quantum-Duel/README.md) |
| **愛情進行時 (Love in Progress)** | 桌面視窗 | Python 3 / Tkinter | 在螢幕上依據心形數學曲線軌跡動態生成多個提示彈窗的趣味程式，具備一鍵退出安全機制。 | [檢視說明](./Love-in-Progress/README.md) |
| **猜數字遊戲 (Guess the number)** | 網頁瀏覽器 | HTML5 / CSS3 / JavaScript | 經典的單機猜數字遊戲，提供即時的高低提示與完整的輸入數值防呆驗證。 | [檢視說明](./Guess-the-number/README.md) |

---

## 快速開始

### 複製專案庫

請先將本專案庫複製到您的本地環境：

```bash
git clone https://github.com/Scorpio-meow/Miao-Playground.git
cd Miao-Playground
```

### 執行網頁版遊戲 (Liquid Cipher / Guess the number)

網頁版遊戲無須進行任何編譯，可直接以瀏覽器開啟各目錄下的 `index.html`。然而，為了獲得更好的瀏覽器安全上下文與完整的載入體驗，推薦使用 Bun 在專案目錄下啟動靜態伺服器：

```bash
# 進入遊戲目錄
cd Liquid-Cipher

# 啟動靜態伺服器
bunx serve .
```

啟動後，請在瀏覽器中造訪終端機所顯示的位址（預設為 `http://localhost:3000`）。

### 執行 Python 遊戲與工具 (Stardust Labyrinth / Quantum Duel / Love in Progress)

執行 Python 專案前，請確保您的系統已安裝 Python 3 執行環境。

```bash
# 進入專案目錄
cd Quantum-Duel

# 執行程式
python "Quantum Duel.py"
```

> [!NOTE]
> 「愛情進行時 (Love in Progress)」需要 Tkinter 繪圖庫支援。若在 Linux 系統下執行遇到缺乏 Tkinter 的錯誤，請使用系統套件管理工具安裝，例如：`sudo apt-get install python3-tk`
