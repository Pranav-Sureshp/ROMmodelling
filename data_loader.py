import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class DuctDataLoader:
    """Handles loading and cleaning of duct-related datasets."""
    
    DEFAULT_COLUMNS = [
        'nodenumber', 'x', 'y', 'z', 
        'vel_mag', 'vel_x', 'vel_y', 'vel_z', 'temperature'
    ]

    def __init__(self, columns=None):
        self.columns = columns if columns is not None else self.DEFAULT_COLUMNS

    def load_file(self, filepath):
        """Reads a single file, handles formatting, and cleans NaN values."""
        print(f"Reading {filepath}...")
        
        # Read data from file
        df = pd.read_csv(
            filepath, 
            sep=',', 
            skipinitialspace=True, 
            header=None, 
            names=self.columns, 
            comment='#',
            na_values=['nan', 'NaN', 'NAN', '']
        )
        
        # Clean and convert data
        df = df.apply(pd.to_numeric, errors='coerce').fillna(0)
        print(f"  Loaded {len(df)} points")
        return df

    def load_multiple(self, file_paths):
        """Helper to load a list of file paths into a list of DataFrames."""
        return [self.load_file(fp) for fp in file_paths]


class DuctVisualizer3D:
    """Handles 3D visualization and generation of scatter plots."""
    
    def __init__(self, title='All 4 Datasets - Temperature Distribution (3D Scatter)'):
        self.fig = plt.figure(figsize=(12, 10))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.title = title
        self._last_scatter = None

    def plot_dataset(self, df, label, cmap='viridis', color_column='temperature', size=6, alpha=0.7):
        """Plots a single dataframe onto the 3D axes."""
        self._last_scatter = self.ax.scatter(
            df['x'], df['y'], df['z'],
            c=df[color_column],
            cmap=cmap,
            s=size,
            alpha=alpha,
            label=label
        )

    def finalize_plot(self, colorbar_label='Temperature', save_path='./strong.png', dpi=100):
        """Applies labels, colorbars, legends, saves, and shows the plot."""
        # Set axes labels and title
        self.ax.set_xlabel('X Coordinate')
        self.ax.set_ylabel('Y Coordinate')
        self.ax.set_zlabel('Z Coordinate')
        self.ax.set_title(self.title)

        # Add a colorbar if data has been plotted
        if self._last_scatter is not None:
            cbar = self.fig.colorbar(self._last_scatter, ax=self.ax, shrink=0.6, pad=0.1)
            cbar.set_label(colorbar_label)

        # Add legend
        self.ax.legend()
        self.fig.tight_layout()
        
        # Save and show
        if save_path:
            plt.savefig(save_path, dpi=dpi)
            print(f"Plot saved to {save_path}")
        
        plt.show()



