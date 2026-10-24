# 無障礙聲明

## 我們的承諾

貓咪遊樂場希望每個人都能找到自己能玩、玩得開心的小遊戲。我們在設計與維護各子專案時參考 [WCAG 2.2](https://www.w3.org/TR/WCAG22/) AA 等級的原則，並誠實揭露每款遊戲目前做不到的地方，讓你在遊玩前就能判斷是否適合自己。

## 目前的無障礙功能

各子專案的無障礙概況如下，詳細內容請見各自的無障礙聲明：

| 子專案 | 介面 | 鍵盤操作 | 螢幕閱讀器 | 詳細聲明 |
| :--- | :--- | :--- | :--- | :--- |
| [液體解鎖 (Liquid Cipher)](https://github.com/Scorpio-meow/Liquid-Cipher) | 網頁 Canvas | ✅ 完整快捷鍵 | ⚠️ 播報移動與提示，無法讀取試管顏色 | [ACCESSIBILITY.md](https://github.com/Scorpio-meow/Liquid-Cipher/blob/main/ACCESSIBILITY.md) |
| [星塵迷宮 (Stardust Labyrinth)](https://github.com/Scorpio-meow/Stardust-Labyrinth) | 終端機純文字 | ✅ WASD + Enter | ⚠️ 可朗讀，但難以理解地圖空間 | [ACCESSIBILITY.md](https://github.com/Scorpio-meow/Stardust-Labyrinth/blob/main/ACCESSIBILITY.md) |
| [量子猜拳 (Quantum Duel)](https://github.com/Scorpio-meow/Quantum-Duel) | 終端機純文字 | ✅ 單一字元 + Enter | ✅ 全部資訊皆為文字 | [ACCESSIBILITY.md](https://github.com/Scorpio-meow/Quantum-Duel/blob/main/ACCESSIBILITY.md) |
| [愛情進行時 (Love in Progress)](https://github.com/Scorpio-meow/Love-in-Progress) | 桌面彈窗 | ⚠️ 退出前需先用滑鼠點選彈窗 | ❌ 不支援 | [ACCESSIBILITY.md](https://github.com/Scorpio-meow/Love-in-Progress/blob/main/ACCESSIBILITY.md) |
| [猜數字遊戲 (Guess the Number)](https://github.com/Scorpio-meow/Guess-the-number) | 網頁表單 | ✅ Tab / Enter | ⚠️ 結果不會自動播報 | [ACCESSIBILITY.md](https://github.com/Scorpio-meow/Guess-the-number/blob/main/ACCESSIBILITY.md) |

本專案庫的說明文件以 Markdown 撰寫，使用標題層級與具標題列的表格，方便螢幕閱讀器導覽。

## 支援的環境

| 類型 | 子專案 | 需求 |
| :--- | :--- | :--- |
| 網頁遊戲 | 液體解鎖、猜數字遊戲 | 最新版的 Chrome、Edge、Firefox、Safari，桌機與行動裝置皆可 |
| 終端機遊戲 | 星塵迷宮、量子猜拳 | Python 3.7 以上，以及能顯示 UTF-8 中文的終端機 |
| 桌面程式 | 愛情進行時 | Python 3 與 Tkinter，Windows、macOS、Linux 桌面環境 |

## 已知限制

我們希望誠實揭露目前做不到的地方，讓你在使用前就能判斷是否適合自己：

- **液體解鎖**：盤面繪製在 `<canvas>` 上，螢幕閱讀器無法讀出試管內的顏色，全盲玩家目前難以獨立遊玩；只有深色主題。
- **星塵迷宮**：ASCII 地圖難以透過螢幕閱讀器理解空間位置。
- **量子猜拳**：介面只有中文，按鍵與行動名稱沒有字面上的關聯。
- **愛情進行時**：會快速產生數百個置頂彈窗鋪滿螢幕，可能讓對光線敏感、有前庭障礙或容易焦慮的人感到不適，也會干擾其他輔助工具。
- **猜數字遊戲**：結果不會自動播報給螢幕閱讀器，部分提示文字的色彩對比不足。

## 回報無障礙問題

如果你在使用時遇到任何障礙，或發現本聲明與實際情況不符，歡迎告訴我們：

- [填寫無障礙問題回報 Issue](https://github.com/Scorpio-meow/Miao-Playground/issues/new?template=accessibility.yml)
- 不方便公開說明時，可寄信至 [yao921024@gmail.com](mailto:yao921024@gmail.com)
- 某款遊戲的問題，也可以直接到該子專案回報：[液體解鎖 (Liquid Cipher)](https://github.com/Scorpio-meow/Liquid-Cipher/issues/new?template=accessibility.yml)、[星塵迷宮 (Stardust Labyrinth)](https://github.com/Scorpio-meow/Stardust-Labyrinth/issues/new?template=accessibility.yml)、[量子猜拳 (Quantum Duel)](https://github.com/Scorpio-meow/Quantum-Duel/issues/new?template=accessibility.yml)、[愛情進行時 (Love in Progress)](https://github.com/Scorpio-meow/Love-in-Progress/issues/new?template=accessibility.yml)、[猜數字遊戲 (Guess the Number)](https://github.com/Scorpio-meow/Guess-the-number/issues/new?template=accessibility.yml)

回報時請盡量說明：

- 遇到障礙的畫面、功能或操作步驟
- 使用的輔助科技或設定（例如螢幕閱讀器名稱與版本、螢幕放大倍率、只使用鍵盤）
- 使用的是哪一款遊戲，以及作業系統、瀏覽器或 Python 版本
- 你預期的結果與實際發生的情況

本專案由個人利用業餘時間維護，無法保證修正時程，但會優先處理讓人完全無法使用的問題。

## 評估方式

本聲明由維護者依照實際程式行為自我評估撰寫，尚未經過第三方正式稽核。

最後更新：2026-10-25
