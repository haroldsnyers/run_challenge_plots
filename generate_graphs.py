import matplotlib.pyplot as plt
import numpy as np


class GenerateGraphs:
    WEEKS = ('week1', 'week2', 'week3', 'week4', 'week5', 'week6', 'week7', 'week8')
    COLORS = ('r', 'g', 'b', 'y')

    def __init__(self, name, km_list, minutes_list=None):
        self.name = name
        self.km_list = km_list
        self.minutes_list = minutes_list

    def generate_bar_chart_km(self):
        title = 'Km per week by session for ' + self.name
        self._generate_bar_chart('km', title, 'Weeks', 'Km')

    def generate_bar_chart_minutes(self):
        title = 'Km per week by session for ' + self.name
        self._generate_bar_chart('minutes', title, 'Weeks', 'minutes')

    def _generate_histogram(self):
        pass
        # Histogram
        # fig_hist, ax_hist = plt.subplots()
        #
        # num_bins = 8
        #
        # # the histogram of the data
        # n, bins, patches = ax_hist.hist(test, num_bins, histtype='bar')
        #
        # # add a 'best fit' line
        # # y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
        # #      np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
        # # ax_hist.plot(bins, y, '--')
        # ax_hist.set_xlabel('Weeks')
        # ax_hist.set_ylabel('Km')
        # ax_hist.set_title(r'Histogram of kilometers of mathieu')
        #
        # # Tweak spacing to prevent clipping of ylabel
        # fig_hist.tight_layout()
        # plt.show()

    def _generate_bar_chart(self, type, title, x_axis, y_axis):
        if type == 'km':
            bar_values = self.km_list
        else:
            bar_values = self.minutes_list

        N = len(bar_values[0])
        width = 0.80 / len(bar_values)  # the width of the bars

        ind = np.arange(N)  # the x locations for the groups

        fig, ax = plt.subplots()

        sessions = [ax.bar(ind + width * x, bar_values[x], width, color=self.COLORS[x]) for x in range(len(bar_values))]

        # add some text for labels, title and axes ticks
        ax.set_ylabel(y_axis)
        ax.set_ylim([0, 20])
        ax.set_xlabel(x_axis)
        ax.set_title(title)
        ax.set_xticks(ind + width)
        ax.set_xticklabels(self.WEEKS)

        legend_param_values = (x for x in sessions)
        legend_param_names = ('Session ' + str(x) for x in range(len(sessions)))

        ax.legend(legend_param_values, legend_param_names)

        def autolabel(rects):
            # attach some text labels
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, '%d' % int(height),
                        ha='center', va='bottom')

        for session in sessions:
            autolabel(session)

        plt.show()
