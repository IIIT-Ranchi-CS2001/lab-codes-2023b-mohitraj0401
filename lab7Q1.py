import matplotlib.pyplot as plt

parties_mp = ['BJP', 'INC', 'BSP', 'Others']
seats_mp = [163, 66, 0, 1]
colors_mp = ['#FFD700', '#FF6347', '#8A2BE2', '#87CEEB']
explode_mp = [0.1, 0, 0, 0] 


parties_rj = ['INC', 'BJP', 'BSP', 'Others']
seats_rj = [69, 115, 2, 13]
colors_rj = ['#FF6347', '#FFD700', '#8A2BE2', '#87CEEB']
explode_rj = [0, 0.1, 0, 0]  

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))


ax1.pie(seats_mp, labels=parties_mp, autopct='%1.1f%%', startangle=140, colors=colors_mp, explode=explode_mp)
ax1.set_title('Madhya Pradesh Assembly Election 2023 Results')


ax2.pie(seats_rj, labels=parties_rj, autopct='%1.1f%%', startangle=140, colors=colors_rj, explode=explode_rj)
ax2.set_title('Rajasthan Assembly Election 2023 Results')


plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
index = range(len(parties_mp))


mp_bars = plt.bar(index, seats_mp, bar_width, label='Madhya Pradesh', color=colors_mp, alpha=0.7)


rj_bars = plt.bar([i + bar_width for i in index], seats_rj, bar_width, label='Rajasthan', color=colors_rj, alpha=0.7)


plt.xlabel('Party')
plt.ylabel('Seats Won')
plt.title('Assembly Elections 2023 - Seat Share Comparison')
plt.xticks([i + bar_width / 2 for i in index], parties_mp)
plt.legend()


plt.tight_layout()
plt.show()
