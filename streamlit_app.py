import streamlit as st
import numpy as np


def create_life_months_grid(life_span, current_age):
    """
    Create a grid representing a person's life in months
    
    :param life_span: Total expected lifespan
    :param current_age: Current age of the person
    :return: NumPy array representing the life grid
    """
    # Total months in the lifespan
    total_months = life_span * 12
    
    # Create the grid
    grid = np.zeros((life_span // 3 + 1, 36), dtype=int)
    
    # Color coding
    # 0: Unused/Future
    # 1: Lived months
    # 2: Current month
    
    # Fill lived months
    current_months_lived = current_age * 12
    for month in range(current_months_lived):
        row = month // 36
        col = month % 36
        grid[row, col] = 1
    
    # Mark current month
    current_row = (current_months_lived - 1) // 36
    current_col = (current_months_lived - 1) % 36
    grid[current_row, current_col] = 2
    
    return grid

def render_life_months(grid):
    """
    Render the life months grid in Streamlit
    
    :param grid: NumPy array of life months
    """
    st.markdown("## Your Life in Months")
    
    # Create columns for better layout
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Color mapping
        color_map = {
            0: 'lightgray',  # Unused/Future
            1: 'blue',       # Lived months
            2: 'red'         # Current month
        }
        
        # Create grid visualization using st.markdown
        grid_html = "<div style='display: grid; grid-template-columns: repeat(36, 1fr); gap: 2px; width: 100%; max-width: 800px;'>"
        for row in grid:
            for cell in row:
                color = color_map[cell]
                grid_html += f"<div style='aspect-ratio: 1; background-color: {color};'></div>"
        grid_html += "</div>"
        
        st.markdown(grid_html, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        ### Grid Legend
        - 🔵 Blue: Months lived
        - 🔴 Red: Current month
        - ⚪ Gray: Future months
        
        Each row = 3 years
        """)

def main():
    # Page configuration
    st.set_page_config(
        page_title="Life in Months Visualizer", 
        page_icon="🕰️",
        layout="wide"
    )
    
    st.title("🌱 Visualize Your Life in Months")
    
    # Create columns for layout
    col1, col2 = st.columns(2)
    
    with col1:
        # Expected lifespan input
        expected_lifespan = st.slider(
            "Expected Lifespan", 
            min_value=50, 
            max_value=120, 
            value=90, 
            step=1,
            help="Adjust the total expected years of life"
        )
    
    with col2:
        # Current age input
        current_age = st.slider(
            "Current Age", 
            min_value=0, 
            max_value=expected_lifespan, 
            value=30, 
            step=1,
            help="Set your current age"
        )
    
    # Generate and render the grid
    life_grid = create_life_months_grid(expected_lifespan, current_age)
    render_life_months(life_grid)
    
    # Metrics section
    col1, col2, col3 = st.columns(3)
    
    months_lived = current_age * 12
    months_total = expected_lifespan * 12
    percentage_lived = (months_lived / months_total) * 100
    
    with col1:
        st.metric("Months Lived", f"{months_lived:,}")
    with col2:
        st.metric("Total Months", f"{months_total:,}")
    with col3:
        st.metric("Percentage of Life", f"{percentage_lived:.2f}%")
    
    # Add a footer
    st.markdown("""
    ---
    💡 Inspired by Wait But Why's visualization of life in months.
    """)

if __name__ == "__main__":
    main()