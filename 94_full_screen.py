import pickle
from math import floor
import ttkbootstrap as ttk

roulette_number = ['0',
                   '32', '15', '19', '4', '21', '2', '25', '17', '34', '6', '27', '13', '36', '11', '30', '8',
                   '23', '10', '5', '24', '16', '33', '1', '20', '14', '31', '9', '22', '18', '29', '7', '28',
                   '12', '35', '3', '26']
roulette_color = ['green',
                  'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black',
                  'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black',
                  'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black']

def calculate_history_offset(rl_number):
    if roulette_color[rl_number] == 'black':
        return 0
    elif roulette_color[rl_number] == 'green':
        return 1
    elif roulette_color[rl_number] == 'red':
        return 2
    else:
        print("Something must be wrong")
        return 99


class MainWindow(ttk.Window):
    def __init__(self):
        super().__init__()
        self.attributes('-fullscreen', True)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # print("Window size = {} x {}".format(screen_width, screen_height))
        # Calculate dimension for the tree-canvas upcoming
        self.canvas_width = screen_width  # Make canvas go full width
        # -------- Retrieve the series of winning_number
        with open('winning_number.pkl', 'rb') as f:
            self.winning_numbers = pickle.load(f)

        print("Retrieve {} winning numbers".format(len(self.winning_numbers)))
        print(self.winning_numbers)

        # -------------------------------------------------------------------------------------------------------------
        # Calculate the unit and height_history
        self.history_number_display = 15  # this should be odd number
        # -------- Get the data
        self.history_latest_number = self.winning_numbers[-1]
        self.history_sequence_number = []
        for i in range(self.history_number_display):
            get_tail_number = self.winning_numbers[len(self.winning_numbers) - 2 - i]
            self.history_sequence_number.append(get_tail_number)
        print("Latest number is {}".format(self.history_latest_number))
        print("Sequence number is {}".format(self.history_sequence_number))
        # The history the latest number is double size, the gap is half of the unit
        self.history_unit = int(floor(screen_width / (2 + (self.history_number_display - 1) +
                                                      (self.history_number_display - 1) / 2)))
        # We want the history unit must be integer and even so that it can divided by 2
        if self.history_unit % 2 == 0:
            self.history_unit = self.history_unit
        else:
            self.history_unit = self.history_unit - 1
        self.history_gap = int(self.history_unit / 2)
        self.history_padding_left = (screen_width - self.history_unit * (2 + (self.history_number_display - 1) +
                                                                         (self.history_number_display - 1) / 2)) / 2
        self.history_padding_top = self.history_padding_left
        self.height_history = 2 * self.history_padding_top + 2 * self.history_unit
        print("Calculated height of history = {}".format(self.height_history))
        print("Calculated history unit = {}".format(self.history_unit))
        print("Calculated history padding left = {}".format(self.history_padding_left))
        self.history_sequence_square = []
        self.history_sequence_text = []
        # -------------------------------------------------------------------------------------------------------------
        # Calculate the unit and height_histogram
        self.histogram_level = 5  # histogram max level is 5 including 0, 1, 2, 3, 4, 5
        self.histogram_bar_offset = 5  # offset of the bar at level 0 is 5 pixels
        self.histogram_num_bar = 37
        self.histogram_bar = []
        self.histogram_square = []
        self.histogram_text = []
        # -------- Calculate the histogram of winning_number
        self.histogram = [0] * len(roulette_number)
        for i in range(len(self.winning_numbers)):
            self.histogram[roulette_number.index(str(self.winning_numbers[i]))] += 1
        print("winning_numbers histogram with min={} max={}".format(min(self.histogram), max(self.histogram)))
        print(self.histogram)
        # The histogram is a bar chart with 37 bars and 36 gap
        # the gap is half of the bar width so total gap is equal 18 bars
        self.histogram_unit = int(floor(screen_width / 55))  # 55 is equal 37 bars and 36 gap
        # We want the histogram unit must be integer and even so that it can divided by 2
        if self.histogram_unit % 2 == 0:
            self.histogram_unit = self.histogram_unit
        else:
            self.histogram_unit = self.histogram_unit - 1
        self.histogram_gap = int(self.histogram_unit / 2)
        self.histogram_padding_left = (screen_width - (55 * self.histogram_unit)) / 2
        self.histogram_padding_top = self.histogram_padding_left
        self.height_histogram = self.histogram_padding_top + (3 * self.histogram_unit) + \
                                (self.histogram_bar_offset + self.histogram_level * self.histogram_unit)
        print("Calculated height of histogram = {}".format(self.height_histogram))
        print("Calculated histogram unit = {}".format(self.histogram_unit))
        # -------------------------------------------------------------------------------------------------------------
        self.height_body = screen_height - self.height_history - self.height_histogram
        print("Calculated height of body = {}".format(self.height_body))
        # -------------------------------------------------------------------------------------------------------------

        # Create canvas history, canvas body and canvas histogram
        self.create_canvas_history().pack()
        self.create_canvas_body().pack()
        self.create_canvas_histogram().pack()

    def create_canvas_history(self) -> ttk.Canvas:
        """ Create canvas history """
        self.canvas_history = ttk.Canvas(self)
        self.canvas_history.config(bg='lightblue')
        self.canvas_history.config(width=self.canvas_width, height=self.height_history)
        self.canvas_history.config(bd=0, relief='ridge')

        # Draw the latest number
        c1 = self.history_padding_left
        d1 = self.history_padding_top + 2*self.history_unit
        c2 = c1 + 2*self.history_unit
        d2 = d1 - 2*self.history_unit
        self.latest_number_square = self.canvas_history.create_rectangle(
            c1, d1, c2, d2, fill=roulette_color[self.history_latest_number])
        center_x = (c1 + c2) / 2
        center_y = (d1 + d2) / 2
        self.latest_number_text = self.canvas_history.create_text(
            center_x, center_y, text=self.history_latest_number,
            fill='white', font=('Helvetica', 96, 'bold'))

        # Draw the sequence number
        start_x = self.history_padding_left + 2 * self.history_unit + self.history_gap
        start_y = self.history_padding_top + 2 * self.history_unit
        for i in range(len(self.history_sequence_number)):
            e1 = start_x + i * (self.history_unit + self.history_gap)
            f1 = start_y - self.history_gap*calculate_history_offset(self.history_sequence_number[i])
            e2 = e1 + self.history_unit
            f2 = f1 - self.history_unit
            square = self.canvas_history.create_rectangle(
                e1, f1, e2, f2, fill=roulette_color[self.history_sequence_number[i]])
            self.history_sequence_square.append(square)
            cen_x = (e1 + e2) / 2
            cen_y = (f1 + f2) / 2
            text = self.canvas_history.create_text(cen_x, cen_y, text=str(self.history_sequence_number[i]),
                                                     fill='white', font=('Helvetica', 48, 'bold'))
            self.history_sequence_text.append(text)
        return self.canvas_history

    def create_canvas_body(self) -> ttk.Canvas:
        """ Create canvas history """
        self.canvas_body = ttk.Canvas(self)
        self.canvas_body.config(bg='lightgreen')
        self.canvas_body.config(width=self.canvas_width, height=self.height_body)
        self.canvas_body.config(bd=0, relief='ridge')

        return self.canvas_body

    def create_canvas_histogram(self) -> ttk.Canvas:
        """ Create canvas histogram """
        self.canvas_histogram = ttk.Canvas(self)
        self.canvas_histogram.config(bg='white')
        self.canvas_histogram.config(width=self.canvas_width, height=self.height_histogram)
        self.canvas_histogram.config(bd=0, relief='ridge')

        # Draw square 1 unit to hold text
        for i in range(self.histogram_num_bar):
            x1 = self.histogram_padding_left + i * (self.histogram_unit + self.histogram_gap)
            y1 = self.histogram_padding_top + (2 * self.histogram_unit) + \
                 (self.histogram_bar_offset + self.histogram_level * self.histogram_unit)
            x2 = x1 + self.histogram_unit
            y2 = y1 - self.histogram_unit

            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2

            a1 = x1
            a2 = x2
            b1 = y1 - (2 * self.histogram_unit)
            b2 = b1 - (self.histogram_bar_offset + self.histogram[i] * self.histogram_unit)

            # Create a rectangle on the canvas and store its reference in the list
            square = self.canvas_histogram.create_rectangle(x1, y1, x2, y2, fill=roulette_color[i])
            self.histogram_square.append(square)
            # Create the text at the middle of the square
            text = self.canvas_histogram.create_text(center_x, center_y, text=roulette_number[i],
                                                     fill='white', font=('Helvetica', 12, 'bold'))
            self.histogram_text.append(text)
            # Create the bars based on histogram
            bar = self.canvas_histogram.create_rectangle(a1, b1, a2, b2, fill=roulette_color[i])
            self.histogram_bar.append(bar)

        print("Canvas histogram size = {} x {}".format(self.canvas_histogram.winfo_reqwidth(),
                                                       self.canvas_histogram.winfo_reqheight()))
        return self.canvas_histogram


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
