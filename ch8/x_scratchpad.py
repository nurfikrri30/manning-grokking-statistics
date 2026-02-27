import matplotlib.pyplot as plt

years = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
cage_films = [1, 2, 2, 2, 1, 1, 2, 3, 4, 1, 4]  # Approximate counts based on the meme data
pool_drownings = [109, 102, 102, 98, 85, 95, 96, 98, 123, 94, 102]

fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Films Nicolas Cage Appeared In', color='tab:blue')
ax1.plot(years, cage_films, color='tab:blue', marker='o', label='Nicolas Cage Films')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('People Who Drowned by Falling Into a Pool', color='tab:red')
ax2.plot(years, pool_drownings, color='tab:red', marker='o', label='Pool Drownings')
ax2.tick_params(axis='y', labelcolor='tab:red')

plt.title('Nicolas Cage Films vs. Pool Drownings by Year (1999–2009)\n(A Famous Spurious Correlation Meme)')
fig.tight_layout()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()