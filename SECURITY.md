# 安全性政策

感謝你協助讓貓咪遊樂場更安全。

## 支援的版本

本專案沒有發佈版本號，安全性修正只會套用在 `main` 分支的最新版本。

| 版本 | 是否支援 |
| :--- | :---: |
| `main` 分支的最新版本 | ✅ |
| 舊的 commit 或自行修改的分支 | ❌ |

## 回報安全性漏洞

> [!CAUTION]
> 請**不要**透過公開的 Issue、Pull Request 或討論回報安全性漏洞，以免在修正前被他人利用。

請使用 GitHub 的私密漏洞回報功能：

1. 前往本專案的 [私密漏洞回報頁面](https://github.com/Scorpio-meow/Miao-Playground/security/advisories/new)。
2. 填寫漏洞說明後送出，內容只有你與維護者看得到。

回報時請盡量提供：

- 漏洞類型與可能造成的影響
- 受影響的檔案路徑或功能
- 重現步驟或概念驗證（PoC）
- 你的執行環境（作業系統、瀏覽器或 Python 版本）
- 建議的修正方式（如有）

## 處理流程

1. 維護者確認收到回報後，會評估問題並與你聯繫，必要時請你補充資訊。
2. 確認為漏洞後，會在私密的 Security Advisory 中進行修正，修正釋出後才公開說明細節。
3. 如果你願意，公告中會列名感謝你的回報。

本專案由個人利用業餘時間維護，無法保證回覆時間，但每一份回報都會被認真看待。

## 範圍

本專案庫是遊戲總覽，只包含說明文件與指向各子專案的 Git 子模組，本身沒有可執行的程式碼。

**遊戲本身的漏洞，請到對應的子專案私密回報：**

| 子專案 | 私密漏洞回報 | 安全性政策 |
| :--- | :--- | :--- |
| [液體解鎖 (Liquid Cipher)](https://github.com/Scorpio-meow/Liquid-Cipher) | [回報](https://github.com/Scorpio-meow/Liquid-Cipher/security/advisories/new) | [SECURITY.md](https://github.com/Scorpio-meow/Liquid-Cipher/blob/main/SECURITY.md) |
| [星塵迷宮 (Stardust Labyrinth)](https://github.com/Scorpio-meow/Stardust-Labyrinth) | [回報](https://github.com/Scorpio-meow/Stardust-Labyrinth/security/advisories/new) | [SECURITY.md](https://github.com/Scorpio-meow/Stardust-Labyrinth/blob/main/SECURITY.md) |
| [量子猜拳 (Quantum Duel)](https://github.com/Scorpio-meow/Quantum-Duel) | [回報](https://github.com/Scorpio-meow/Quantum-Duel/security/advisories/new) | [SECURITY.md](https://github.com/Scorpio-meow/Quantum-Duel/blob/main/SECURITY.md) |
| [愛情進行時 (Love in Progress)](https://github.com/Scorpio-meow/Love-in-Progress) | [回報](https://github.com/Scorpio-meow/Love-in-Progress/security/advisories/new) | [SECURITY.md](https://github.com/Scorpio-meow/Love-in-Progress/blob/main/SECURITY.md) |
| [猜數字遊戲 (Guess the Number)](https://github.com/Scorpio-meow/Guess-the-number) | [回報](https://github.com/Scorpio-meow/Guess-the-number/security/advisories/new) | [SECURITY.md](https://github.com/Scorpio-meow/Guess-the-number/blob/main/SECURITY.md) |

**屬於本專案庫的回報範圍：**

- `.gitmodules` 中的子模組網址被指向非官方或惡意的來源
- 說明文件中的指令可能對使用者的電腦造成安全風險
