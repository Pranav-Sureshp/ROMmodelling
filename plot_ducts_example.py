from data_loader import DuctDataLoader, DuctVisualizer3D


    # Define Configurations
file_paths = [
        '../duct_wall',  
        '../inner_fluid',
        '../outer_fluid',
        '../pipe_wall'
    ]
dataset_labels = ['Case 1', 'Case 2', 'Case 3', 'Case 4']
colors = ['viridis', 'plasma', 'cividis_r', 'coolwarm']

    # 1. Load Data
loader = DuctDataLoader()
dataframes = loader.load_multiple(file_paths)

    # 2. Visualize Data
visualizer = DuctVisualizer3D()
    
for i, df in enumerate(dataframes):
        # Using colors[0] to mimic your original logic, or change to colors[i] for variety
    visualizer.plot_dataset(df, label=dataset_labels[i], cmap=colors[0])
    
    # 3. Render and Save
visualizer.finalize_plot()