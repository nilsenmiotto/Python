import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


BASE_DIR = Path(__file__).parent


def line_plot():
	x = np.linspace(0, 2, 100)
	fig, ax = plt.subplots(figsize=(6, 3), layout="constrained")
	ax.plot(x, x, label="linear")
	ax.plot(x, x ** 2, label="quadratic")
	ax.plot(x, x ** 3, label="cubic")
	ax.set_xlabel("x")
	ax.set_ylabel("y")
	ax.set_title("Line plot")
	ax.legend()
	fig.savefig(BASE_DIR / "line_plot_saida.png")
	plt.close(fig)


def scatter_plot():
	rng = np.random.default_rng(7)
	x = rng.normal(loc=5, scale=2, size=100)
	y = rng.normal(loc=5, scale=2, size=100)
	sizes = rng.integers(20, 200, size=100)
	colors = rng.random(100)

	fig, ax = plt.subplots(figsize=(5, 4), layout="constrained")
	scatter = ax.scatter(x, y, s=sizes, c=colors, cmap="viridis", alpha=0.7)
	ax.set_title("Scatter com cores e tamanhos")
	ax.set_xlabel("x")
	ax.set_ylabel("y")
	fig.colorbar(scatter, ax=ax, label="intensidade")
	fig.savefig(BASE_DIR / "scatter_plot_saida.png")
	plt.close(fig)


def bar_chart():
	categorias = ["A", "B", "C", "D"]
	valores = [12, 7, 18, 5]

	fig, ax = plt.subplots(figsize=(6, 3), layout="constrained")
	ax.bar(categorias, valores, color="#4c72b0")
	ax.set_title("Bar chart")
	ax.set_ylabel("valor")
	ax.margins(y=0.1)
	for x, val in zip(categorias, valores):
		ax.text(x, val + 0.5, f"{val}", ha="center")
	fig.savefig(BASE_DIR / "bar_chart_saida.png")
	plt.close(fig)


def histogram():
	rng = np.random.default_rng(3)
	dados = rng.normal(loc=0, scale=1, size=1000)

	fig, ax = plt.subplots(figsize=(6, 3.5), layout="constrained")
	ax.hist(dados, bins=30, color="#55a868", edgecolor="black", alpha=0.8)
	ax.set_title("Histograma")
	ax.set_xlabel("valor")
	ax.set_ylabel("frequencia")
	fig.savefig(BASE_DIR / "histograma_saida.png")
	plt.close(fig)


def heatmap():
	rng = np.random.default_rng(1)
	data = rng.normal(size=(10, 12))

	fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")
	img = ax.imshow(data, cmap="coolwarm", aspect="auto")
	ax.set_title("Heatmap simples")
	ax.set_xlabel("coluna")
	ax.set_ylabel("linha")
	fig.colorbar(img, ax=ax, label="valor")
	fig.savefig(BASE_DIR / "heatmap_saida.png")
	plt.close(fig)


def subplots_grid():
	x = np.linspace(0, 2 * np.pi, 200)
	fig, axes = plt.subplots(2, 2, figsize=(8, 6), layout="constrained", sharex=True)

	axes[0, 0].plot(x, np.sin(x), color="#4c72b0")
	axes[0, 0].set_title("sin(x)")

	axes[0, 1].plot(x, np.cos(x), color="#dd8452")
	axes[0, 1].set_title("cos(x)")

	axes[1, 0].plot(x, np.tan(x), color="#55a868")
	axes[1, 0].set_ylim(-3, 3)
	axes[1, 0].set_title("tan(x) recortado")

	axes[1, 1].plot(x, np.sin(x) * np.cos(x), color="#c44e52")
	axes[1, 1].set_title("sin(x) * cos(x)")

	for ax in axes.flat:
		ax.grid(True, alpha=0.3)
		ax.set_xlabel("x")
		ax.set_ylabel("y")

	fig.savefig(BASE_DIR / "subplots_trigonometria_saida.png")
	plt.close(fig)


if __name__ == "__main__":
	line_plot()
	scatter_plot()
	bar_chart()
	histogram()
	heatmap()
	subplots_grid()