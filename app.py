import gradio as gr
import pandas as pd

# --- 1. THE AI BRAIN (Simulation Logic) ---
def get_risk_analysis(intensity, stability):
    # Simulating LSTM-Autoencoder logic
    error = (10 - intensity) + (10 - stability)
    risk_percent = min(max(error * 10, 0), 100)
    
    status = "ANOMALY DETECTED" if risk_percent > 50 else "PATTERN NORMAL"
    message = f"Risk Score: {risk_percent}% | Status: {status}"
    
    # Generate data with an explicit Index for the chart
    history = [12, 15, 14, 18, 20, 22, 21, 25, 28, 30, 32, risk_percent]
    chart_data = pd.DataFrame({
        "Index": range(len(history)), 
        "Reconstruction Error Index": history
    })
    
    return message, chart_data

# --- 2. THE GRADIO UI ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 👃 NeuroScent AI")
    gr.Markdown("### Early-Stage Neurodegenerative Screening System")
    gr.Markdown("---")
    
    with gr.Row():
        with gr.Column():
            intensity = gr.Slider(0, 10, value=8.5, label="Inhalation Peak Intensity")
            stability = gr.Slider(0, 10, value=9.0, label="Rhythm Consistency")
            btn = gr.Button("Run Diagnostic Analysis", variant="primary")
            
        with gr.Column():
            output_text = gr.Textbox(label="Diagnostic Result")
            # Explicitly linked to the "Index" column created in the dataframe
            output_plot = gr.LinePlot(
                label="Longitudinal Health Trend", 
                x="Index", 
                y="Reconstruction Error Index",
                tooltip=["Index", "Reconstruction Error Index"]
            )
            
    gr.Markdown("---")
    gr.Markdown(
        "**DISCLAIMER:** NeuroScent AI is an experimental screening prototype. "
        "This tool does not provide a medical diagnosis. Consult a professional."
    )

    # Logic connection
    btn.click(
        fn=get_risk_analysis, 
        inputs=[intensity, stability], 
        outputs=[output_text, output_plot]
    )

# --- 3. EXECUTION ---
if __name__ == "__main__":
    demo.launch()