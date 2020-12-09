import matplotlib.pyplot as plt
import numpy as np
import openpyxl

excel_document = openpyxl.load_workbook('Loutres.xlsx')

sheet_names = excel_document.sheetnames
print(sheet_names)

pf_sheet = excel_document[sheet_names[1]]

print(pf_sheet.cell(row=2, column=20).value)

list_names = [pf_sheet.cell(row=1, column=x).value for x in range(4, 28)]
list_names_columns = [x for x in range(4, 28)]

dict_names = dict(zip(list_names, list_names_columns))


def retrieve_values(sheet, name, x):
    return sheet.cell(row=x, column=dict_names[name]).value if sheet.cell(row=x, column=dict_names[
        name]).value is not None else 0


start, end = 2, 59
matthieu_values = [
    [retrieve_values(pf_sheet, 'Mathieu', x) for x in range(start, end, 8)],
    [retrieve_values(pf_sheet, 'Mathieu', x) for x in range(start + 2, end + 2, 8)],
    [retrieve_values(pf_sheet, 'Mathieu', x) for x in range(start + 4, end + 4, 8)],
    [retrieve_values(pf_sheet, 'Mathieu', x) for x in range(start + 6, end + 6, 8)],
]
print(matthieu_values)

test = [
    [retrieve_values(pf_sheet, 'Mathieu', x),
     retrieve_values(pf_sheet, 'Mathieu', x + 2),
     retrieve_values(pf_sheet, 'Mathieu', x + 4),
     retrieve_values(pf_sheet, 'Mathieu', x + 6)] for x in range(start, end, 8)]

print(test)

# Histogram
fig_hist, ax_hist = plt.subplots()

num_bins = 8

# the histogram of the data
n, bins, patches = ax_hist.hist(test, num_bins, histtype='bar')

# add a 'best fit' line
# y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
#      np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
# ax_hist.plot(bins, y, '--')
ax_hist.set_xlabel('Weeks')
ax_hist.set_ylabel('Km')
ax_hist.set_title(r'Histogram of kilometers of mathieu')

# Tweak spacing to prevent clipping of ylabel
fig_hist.tight_layout()
plt.show()

# bar chart
N = 8

width = 0.15  # the width of the bars

ind = np.arange(N)  # the x locations for the groups

fig, ax = plt.subplots()

session1 = ax.bar(ind, matthieu_values[0], width, color='r')
session2 = ax.bar(ind + width, matthieu_values[1], width, color='g')
session3 = ax.bar(ind + 2 * width, matthieu_values[2], width, color='b')
session4 = ax.bar(ind + 3 * width, matthieu_values[3], width, color='y')

# add some text for labels, title and axes ticks
ax.set_ylabel('km')
ax.set_ylim([0, 20])
ax.set_xlabel('Weeks')
ax.set_title('km per week by session')
ax.set_xticks(ind + width)
ax.set_xticklabels(('week1', 'week2', 'week3', 'week4', 'week5', 'week6', 'week7', 'week8'))

ax.legend((session1[0], session2[0], session3[0], session4[0]),
          ('Session1', 'Session 2', 'Session 3', 'Session 4'))


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, '%d' % int(height),
                ha='center', va='bottom')


autolabel(session1)
autolabel(session2)
autolabel(session3)
autolabel(session4)

plt.show()
