
def tensor_to_latex(tensor):
    """
    Convert a 1D or 2D PyTorch tensor to a LaTeX bmatrix string

    Example:
        ```python
        import torch
        from utils import tensor_to_latex
        from IPython.display import display, Math

        tensor = torch.tensor([1, 2, 3, 4, 5])
        latex_tensor = tensor_to_latex(tensor)
        display(Math(f"\\mathrm{{tensor}} = {latex_tensor}"))
        ```
    Args:
        tensor (torch.Tensor): A PyTorch tensor

    Returns:
        str: A LaTeX bmatrix string
    """
    if tensor.dim() == 1:
        # Convert 1D tensor to a 2D column vector for display
        tensor = tensor.unsqueeze(1)
    
    latex_str = "\\begin{bmatrix}\n"
    for row in tensor:
        latex_str += " & ".join([f"{val.item():.3f}" for val in row]) + " \\\\\n"
    latex_str += "\\end{bmatrix}"
    return latex_str

