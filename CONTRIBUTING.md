# 貢獻指南

感謝你願意花時間改進貓咪遊樂場！本文件說明回報問題、提出建議與提交程式碼的流程。

參與本專案即表示你同意遵守[行為準則](./CODE_OF_CONDUCT.md)。

## 這個專案庫的定位

貓咪遊樂場是一個總覽專案庫，每款遊戲都是獨立的 GitHub 專案，並以 Git 子模組（submodule）的形式收錄在這裡。

**遊戲本身的錯誤、建議與程式碼修改，請到對應的子專案提交：**

| 子專案 | Issue | 貢獻指南 |
| :--- | :--- | :--- |
| [液體解鎖 (Liquid Cipher)](https://github.com/Scorpio-meow/Liquid-Cipher) | [回報](https://github.com/Scorpio-meow/Liquid-Cipher/issues/new/choose) | [CONTRIBUTING.md](https://github.com/Scorpio-meow/Liquid-Cipher/blob/main/CONTRIBUTING.md) |
| [星塵迷宮 (Stardust Labyrinth)](https://github.com/Scorpio-meow/Stardust-Labyrinth) | [回報](https://github.com/Scorpio-meow/Stardust-Labyrinth/issues/new/choose) | [CONTRIBUTING.md](https://github.com/Scorpio-meow/Stardust-Labyrinth/blob/main/CONTRIBUTING.md) |
| [量子猜拳 (Quantum Duel)](https://github.com/Scorpio-meow/Quantum-Duel) | [回報](https://github.com/Scorpio-meow/Quantum-Duel/issues/new/choose) | [CONTRIBUTING.md](https://github.com/Scorpio-meow/Quantum-Duel/blob/main/CONTRIBUTING.md) |
| [愛情進行時 (Love in Progress)](https://github.com/Scorpio-meow/Love-in-Progress) | [回報](https://github.com/Scorpio-meow/Love-in-Progress/issues/new/choose) | [CONTRIBUTING.md](https://github.com/Scorpio-meow/Love-in-Progress/blob/main/CONTRIBUTING.md) |
| [猜數字遊戲 (Guess the Number)](https://github.com/Scorpio-meow/Guess-the-number) | [回報](https://github.com/Scorpio-meow/Guess-the-number/issues/new/choose) | [CONTRIBUTING.md](https://github.com/Scorpio-meow/Guess-the-number/blob/main/CONTRIBUTING.md) |

**本專案庫**只負責總覽 README、子模組設定與共用的社群文件，相關的問題與修改才在這裡提交。

## 目錄

- [回報問題](#回報問題)
- [提出功能建議](#提出功能建議)
- [開發環境](#開發環境)
- [提交 Pull Request](#提交-pull-request)
- [Commit 訊息規範](#commit-訊息規範)
- [程式碼風格](#程式碼風格)
- [測試](#測試)
- [無障礙](#無障礙)
- [授權](#授權)

## 回報問題

- 回報前請先搜尋[現有 Issue](https://github.com/Scorpio-meow/Miao-Playground/issues)，避免重複。
- 請使用對應的 Issue 範本：**錯誤回報**、**功能建議**或**無障礙問題回報**，並盡量填寫重現步驟與執行環境。
- 安全性漏洞請**不要**公開回報，請依照[安全性政策](./SECURITY.md)私下回報。

## 提出功能建議

- 請先說明想解決的問題與使用情境，再提出你建議的做法。
- 較大的改動請先開 Issue 討論，確認方向後再動手，避免白費功夫。

## 開發環境

複製時請加上 `--recurse-submodules`，才會一併下載所有子專案：

```bash
git clone --recurse-submodules https://github.com/<你的帳號>/Miao-Playground.git
cd Miao-Playground
```

如果已經複製過，但子專案資料夾是空的，請執行：

```bash
git submodule update --init --recursive
```

各子專案的執行方式請參考 [README 的快速開始](./README.md#快速開始)。

在本專案庫常見的修改有三種：

- **更新 README 總覽**：例如修正說明、補充子專案簡介。
- **更新子模組指標**：子專案合併新功能後，將子模組更新到最新的 commit：

  ```bash
  git submodule update --remote <子專案資料夾>
  ```

- **新增一款遊戲**：
  1. 先開 Issue 提出並討論。
  2. 遊戲需要是獨立的 GitHub 專案，並具備 README、LICENSE 與完整的社群文件（CONTRIBUTING、CODE_OF_CONDUCT、SECURITY、ACCESSIBILITY、Issue 與 PR 範本）。
  3. 以 `git submodule add <專案網址>` 加入，並在 README 的「專案導覽」表格中補上一列。

## 提交 Pull Request

1. Fork 本專案，並從 `main` 建立新分支，建議命名為 `feat/簡短描述`、`fix/簡短描述` 或 `docs/簡短描述`。
2. 完成修改後，依照下方[測試](#測試)章節自行驗證。
3. 依照[Commit 訊息規範](#commit-訊息規範)撰寫 commit 訊息。
4. 推送分支並建立 Pull Request，完整填寫 PR 範本中的檢查清單。
5. 一個 PR 只處理一件事；不相關的修改請拆成多個 PR，方便審查。

維護者審查時可能會請你調整內容，這是正常的協作過程，感謝你的耐心。

## Commit 訊息規範

本專案採用 [Conventional Commits](https://www.conventionalcommits.org/zh-hant/v1.0.0/) 格式：

```text
<type>(<scope>): <描述>
```

| type | 用途 |
| :--- | :--- |
| `feat` | 新增功能 |
| `fix` | 修正錯誤 |
| `docs` | 只修改文件 |
| `style` | 不影響邏輯的格式調整 |
| `refactor` | 不改變行為的重構 |
| `perf` | 效能改善 |
| `test` | 新增或修改測試 |
| `chore` | 其他雜項（例如設定檔） |

`<scope>` 可省略，描述請用中文或英文簡潔說明「做了什麼」，例如：

```text
docs: 更新專案導覽中液體解鎖的簡介
```

## 程式碼風格

本專案庫以 Markdown 文件為主：

- 沿用 README 既有的標題層級、表格格式與 `---` 分隔線。
- 指向子專案內容的連結請使用完整的 GitHub 網址；子模組在 GitHub 上會顯示為指向特定 commit 的連結，相對路徑無法開啟子專案中的檔案。
- 子模組指標只能指向已存在於子專案 `main` 分支上的 commit。

## 測試

送出 PR 前請手動確認：

- [ ] README 與文件中的連結都能正常開啟
- [ ] `git submodule status` 列出的 commit 都存在於各子專案的 `main` 分支
- [ ] 依照 README 的「快速開始」步驟，可以從頭複製並執行至少一款遊戲

## 無障礙

新功能請一併考量[無障礙聲明](./ACCESSIBILITY.md)中的承諾，例如在 README 中清楚標示每款遊戲的執行環境、新增的遊戲也要附上無障礙聲明。

## 授權

提交貢獻即表示你同意你的貢獻以本專案的 [MIT License](./LICENSE) 授權釋出。
