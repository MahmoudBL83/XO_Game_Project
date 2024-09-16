import tkinter as tk
from tkinter import messagebox

# كلاس لوحة اللعبة (GameBoard)
class GameBoard:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        # إنشاء 3x3 أزرار تمثل شبكة اللعبة
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        """إنشاء الأزرار في نافذة tkinter"""
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 40), width=5, height=2,
                                   command=lambda r=row, c=col: self.game.play_turn(r, c))
                button.grid(row=row, column=col)  # وضع الأزرار في الشبكة
                self.buttons[row][col] = button

    def update_board(self, row, col, symbol):
        """تحديث الزر عند لعب اللاعب"""
        self.buttons[row][col].config(text=symbol)

    def disable_buttons(self):
        """تعطيل الأزرار بعد انتهاء اللعبة"""
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

# كلاس اللاعب (Player)
class Player:
    def __init__(self, name, symbol):
        self.name = name  # اسم اللاعب
        self.symbol = symbol  # رمز اللاعب (X أو O)

# كلاس اللعبة (XOGame)
class XOGame:
    def __init__(self, root):
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.current_player_index = 0  # يبدأ اللاعب الأول
        self.board = [["" for _ in range(3)] for _ in range(3)]  # لوحة 3x3 فارغة
        self.moves_count = 0  # عداد الحركات
        self.game_board = GameBoard(root, self)  # واجهة اللعبة

    def play_turn(self, row, col):
        """تنفيذ حركة اللاعب"""
        if self.board[row][col] == "":  # التحقق إذا كانت الخلية فارغة
            current_player = self.players[self.current_player_index]
            self.board[row][col] = current_player.symbol  # وضع رمز اللاعب في الخلية
            self.game_board.update_board(row, col, current_player.symbol)  # تحديث واجهة المستخدم
            self.moves_count += 1  # زيادة عداد الحركات

            if self.check_winner(current_player.symbol):  # التحقق من الفائز
                messagebox.showinfo("انتهاء اللعبة", f"{current_player.name} فاز!")
                self.game_board.disable_buttons()
            elif self.moves_count == 9:  # إذا امتلأت اللوحة بدون فائز
                messagebox.showinfo("انتهاء اللعبة", "التعادل!")
                self.game_board.disable_buttons()
            else:
                self.current_player_index = 1 - self.current_player_index  # تبديل اللاعبين

    def check_winner(self, symbol):
        # التحقق من الصفوف
        for row in self.board:
            if row[0] == row[1] == row[2] == symbol:
                return True

        # التحقق من الأعمدة
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == symbol:
                return True

        # التحقق من الأقطار
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol:
            return True

        return False


# تشغيل البرنامج الرئيسي
if __name__ == "__main__":
    root = tk.Tk()  # إنشاء نافذة tkinter
    root.title("XO Game")  # عنوان النافذة
    game = XOGame(root)  # إنشاء كائن اللعبة
    root.mainloop()  # بدء الحلقة الرئيسية للتطبيق
