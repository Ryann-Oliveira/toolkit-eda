import matplotlib.pyplot as plt
def readable(plot):
    plt.figure(figsize=(16,8))
    plot()
    plt.title(input("Title: "))
    plt.show()
    
