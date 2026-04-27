import py5
import pandas as pd
import numpy as np
import os

class SymphonyPlayer:
    def __init__(self, path):
        print(f"Loading High-Fidelity Symphony: {path}")
        self.df = pd.read_parquet(path)
        self.total_frames = len(self.df)
        self.current_frame = 0
        self.is_paused = False
        self.fase_cols = [c for c in self.df.columns if c.startswith('fase_')]

def setup():
    py5.size(1280, 800)
    py5.window_title("Harpia Quantum - SPHY Absolute Fidelity Viewer")
    
    global player
    # Automatic search for the Breakthrough Engine output
    target = "sphy_absolute_fidelity.parquet"
    path = target if os.path.exists(target) else ([f for f in os.listdir('.') if f.endswith('.parquet')] + [None])[0]
    
    if not path:
        print("ERROR: Dataset not found. Please run the Breakthrough Engine first!"); py5.exit_sketch(); return

    player = SymphonyPlayer(path)
    py5.color_mode(py5.HSB, 360, 100, 100, 100)
    py5.ellipse_mode(py5.CENTER)
    py5.text_font(py5.create_font("SansSerif", 14))

def draw():
    # Reduced persistence background to highlight vector precision
    py5.background(260, 90, 5, 25) 
    py5.translate(py5.width / 2, py5.height / 2)
    
    data = player.df.iloc[player.current_frame]
    sync = data['t_sphy_coherence']
    
    # 1. Background Gravity Well (Simulates curvature density)
    draw_gravity_well(sync)
    
    # 2. Central Coherence Node (The Xi Nucleus)
    draw_core(sync)
    
    # 3. Synchronized Phase Vectors
    for i, col in enumerate(player.fase_cols):
        draw_phase_node(data[col], i, sync)
        
    # 4. Sub-Planckian Monitoring HUD
    draw_hud(player.current_frame, sync, player.is_paused)
    
    if not player.is_paused:
        player.current_frame = (player.current_frame + 1) % player.total_frames

def draw_gravity_well(sync):
    py5.no_fill()
    py5.stroke_weight(1)
    # Field lines stabilizing as fidelity increases
    for j in range(5):
        alpha = py5.remap(sync, 0, 1, 5, 20)
        py5.stroke(200, 80, 100, alpha)
        r = 300 + j * 50
        py5.ellipse(0, 0, r, r)

def draw_core(sync):
    py5.no_stroke()
    # If fidelity is ultra-high, the core pulses in Goldberg Gold
    if sync > 0.9999:
        py5.fill(50, 90, 100, 90)
    else:
        py5.fill(190, 100, 100, 70)
        
    size = 140 + (sync * 50)
    py5.ellipse(0, 0, size, size)
    
    # Constructive interference glow
    for s in range(3):
        py5.fill(50, 80, 100, 10)
        py5.ellipse(0, 0, size + s*40, size + s*40)

def draw_phase_node(fase, idx, sync):
    # Radius respecting the Inverse Square Law in visualization
    r = 180 + (idx * 32)
    x, y = r * np.cos(fase), r * np.sin(fase)
    
    # Color transition to absolute white light at maximum fidelity
    sat = py5.remap(sync, 0, 1, 100, 0)
    bright = py5.remap(sync, 0, 1, 80, 100)
    
    py5.stroke(200, sat, bright, 60)
    py5.stroke_weight(2)
    py5.line(0, 0, x, y)
    
    py5.no_stroke()
    py5.fill(200, sat, 100)
    py5.ellipse(x, y, 10, 10)

def draw_hud(frame, sync, paused):
    py5.reset_matrix()
    
    # Lateral Telemetry Panel
    py5.fill(0, 0, 15, 80)
    py5.rect(20, 20, 340, 140, 8)
    
    py5.fill(0, 0, 100)
    py5.text(f"PLANCK FRAME: {frame} / {player.total_frames}", 40, 50)
    
    # Critical Symbiosis Alert
    if sync > 0.999999:
        py5.fill(50, 100, 100)
        status = "STATE: ABSOLUTE SYMBIOSIS (7 NINES)"
    elif sync > 0.99:
        py5.fill(120, 80, 100)
        status = "STATE: STABLE COHERENCE"
    else:
        py5.fill(0, 0, 100)
        status = "STATE: SYNCHRONIZING GRID..."

    py5.text(f"SPHY FIDELITY: {sync:.10f}", 40, 80)
    py5.text(status, 40, 110)
    
    # Tensor Progress Bar
    py5.no_fill()
    py5.stroke(0, 0, 100, 30)
    py5.rect(40, 125, 300, 10)
    py5.fill(py5.remap(sync, 0, 1, 0, 120), 80, 100)
    py5.rect(40, 125, sync * 300, 10)

    # Controls Legend
    py5.fill(0, 0, 100, 40)
    py5.text("[SPACE] Toggle Pause | [ARROWS] Temporal Navigation", 40, py5.height - 30)

def key_pressed():
    if py5.key == ' ': player.is_paused = not player.is_paused
    if py5.key == py5.CODED:
        step = 25
        if py5.key_code == py5.RIGHT: player.current_frame = (player.current_frame + step) % player.total_frames
        if py5.key_code == py5.LEFT: player.current_frame = (player.current_frame - step) % player.total_frames

if __name__ == "__main__":
    py5.run_sketch()
