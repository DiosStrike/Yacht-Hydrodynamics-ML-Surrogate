from flask import Flask, render_template_string, jsonify, request
import time
import threading
import numpy as np

app = Flask(__name__)

# --- [Engineering Logic: ML Surrogate Model] ---
def surrogate_predict(params):
    """
    Simulated ML Inference for Residuary Resistance (Rr).
    Non-linear model based on Delft Systematic Yacht Hull Series.
    """
    # High-sensitivity to Froude Number (Wave-making resistance)
    term_speed = params['fr']**3.5 * 220 
    term_form = (params['pc'] * 1.5) + (params['ld'] * 0.5)
    term_ratio = (params['lb'] * 0.3) + (params['bdr'] * 0.4)
    term_buoyancy = abs(params['lc'] + 2.1) * 0.5
    
    # Stochastic output for simulation realism (Physical micro-noise)
    prediction = term_speed + term_form + term_ratio + term_buoyancy
    return round(prediction + np.random.normal(0, 0.005), 4)

# --- [Decision Logic: 3-Tier Alert System] ---
def get_decision_logic(rr, carbon, fr):
    """
    Three-tier Engineering Alert System: Green (Stable) | Yellow (Caution) | Red (Critical)
    """
    if carbon > 30 or rr > 28:
        return "CRITICAL: High carbon intensity. Immediate speed reduction required."
    elif carbon > 22 or rr > 23:
        return "CAUTION: Efficiency declining. Monitor fuel consumption and vibrations."
    elif carbon < 12 and fr < 0.22:
        return "OPTIMAL: System operating at peak efficiency. Low ESG impact."
    else:
        return "STABLE: Propulsion parameters within standard operating range."

class MarineDigitalTwin:
    def __init__(self):
        self.is_autoplay = False
        self.params = {
            'lc': -2.3, 'pc': 0.55, 'ld': 4.5, 'bdr': 3.2, 'lb': 2.8, 'fr': 0.30
        }
        self.target_fr = 0.30 
        self.history = []
        
        # Start background IoT Telemetry thread
        threading.Thread(target=self._run_telemetry, daemon=True).start()

    def _run_telemetry(self):
        dt = 0.5; theta = 0.8; sigma = 0.006
        while True:
            if self.is_autoplay:
                drift = theta * (self.target_fr - self.params['fr']) * dt
                diffusion = sigma * np.random.normal()
                self.params['fr'] += (drift + diffusion)
                self.params['fr'] = max(0.05, min(0.6, self.params['fr']))
                
                rr = surrogate_predict(self.params)
                carbon = round(rr * self.params['fr'] * 2.5, 3)
                recommendation = get_decision_logic(rr, carbon, self.params['fr'])
                
                data_point = {
                    "time": time.strftime("%H:%M:%S"),
                    "rr": rr,
                    "carbon": carbon,
                    "recommendation": recommendation,
                    "fr_val": round(self.params['fr'], 4)
                }
                self.history.append(data_point)
                if len(self.history) > 30: self.history.pop(0)
            time.sleep(dt)

twin_system = MarineDigitalTwin()

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, params=twin_system.params)

@app.route('/api/update_params', methods=['POST'])
def update_params():
    new_data = request.json
    twin_system.params.update(new_data)
    if 'fr' in new_data: twin_system.target_fr = new_data['fr']
    
    rr = surrogate_predict(twin_system.params)
    carbon = round(rr * twin_system.params['fr'] * 2.5, 3)
    recommendation = get_decision_logic(rr, carbon, twin_system.params['fr'])
    return jsonify({"rr": rr, "carbon": carbon, "recommendation": recommendation})

@app.route('/api/telemetry')
def get_telemetry():
    return jsonify(twin_system.history)

@app.route('/api/toggle_system', methods=['POST'])
def toggle_system():
    twin_system.is_autoplay = not twin_system.is_autoplay
    return jsonify({"active": twin_system.is_autoplay})

# --- UI Template: 3-6-3 Layout with Vertical Wave Simulation ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Yacht Digital Twin | AI Engineering</title>
    <link href="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/5.3.1/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { background: #fdfdfd; font-family: 'Segoe UI', sans-serif; color: #2d3748; }
        .module-card { border: 1px solid #e2e8f0; border-radius: 8px; background: #fff; padding: 20px; margin-bottom: 20px; transition: 0.3s; height: 100%; }
        .module-card:hover { border-color: #3182ce; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05); }
        .btn-custom { border: 2px solid #3182ce; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
        .label-container { display: flex; justify-content: space-between; font-size: 0.72rem; font-weight: 700; color: #4a5568; margin-bottom: 2px; }
        
        /* Side-View Wave Visualization Window */
        .viz-container { 
            height: 180px; 
            background: linear-gradient(to bottom, #87CEEB 0%, #87CEEB 50%, #1E90FF 50%, #00008B 100%);
            border-radius: 8px; position: relative; overflow: hidden; margin-bottom: 15px; border: 1px solid #2c5282;
        }
        
        .decision-box { background: #f7fafc; border-left: 5px solid #cbd5e0; padding: 12px; font-size: 0.85rem; min-height: 110px; transition: 0.5s; }
        .highlight-red { border-left-color: #e53e3e; color: #c53030; background: #fff5f5; }
        .highlight-yellow { border-left-color: #ecc94b; color: #b7791f; background: #fffff0; }
        .highlight-green { border-left-color: #48bb78; color: #2f855a; background: #f0fff4; }
    </style>
</head>
<body>
    <div class="container-fluid px-5 py-4">
        <div class="d-flex justify-content-between align-items-end mb-4 border-bottom pb-3">
            <div>
                <h3 class="fw-bold mb-1">Yacht Hydrodynamics Digital Twin</h3>
                <p class="text-muted small mb-0">Real-time Performance Monitoring & ESG Decision Pipeline</p>
            </div>
            <div class="d-flex flex-column align-items-end">
                <div class="text-muted small mb-2">Principal Investigator: <strong>Tanghao Chen (Dios)</strong></div>
                <button class="btn btn-outline-primary btn-custom btn-sm" id="mainBtn" onclick="toggleTelemetry()">Start Telemetry</button>
            </div>
        </div>
        
        <div class="row g-4">
            <div class="col-lg-3">
                <div class="module-card">
                    <h6 class="fw-bold mb-3 border-start border-4 border-primary ps-2">Design Studio</h6>
                    <div class="slider-wrap mb-3"><div class="label-container"><span>LC - Long. Pos. Center of Buoyancy</span><span id="v-lc">-2.3</span></div><input type="range" class="form-range" id="lc" min="-5" max="0" step="0.1" value="-2.3" oninput="syncParams()"></div>
                    <div class="slider-wrap mb-3"><div class="label-container"><span>PC - Prismatic Coefficient</span><span id="v-pc">0.55</span></div><input type="range" class="form-range" id="pc" min="0.5" max="0.8" step="0.01" value="0.55" oninput="syncParams()"></div>
                    <div class="slider-wrap mb-3"><div class="label-container"><span>LD - Length-Displacement Ratio</span><span id="v-ld">4.5</span></div><input type="range" class="form-range" id="ld" min="3" max="6" step="0.1" value="4.5" oninput="syncParams()"></div>
                    <div class="slider-wrap mb-3"><div class="label-container"><span>BDr - Beam-Draught Ratio</span><span id="v-bdr">3.2</span></div><input type="range" class="form-range" id="bdr" min="2" max="5" step="0.1" value="3.2" oninput="syncParams()"></div>
                    <div class="slider-wrap mb-3"><div class="label-container"><span>LB - Length-Beam Ratio</span><span id="v-lb">2.8</span></div><input type="range" class="form-range" id="lb" min="2" max="5" step="0.1" value="2.8" oninput="syncParams()"></div>
                    <div class="slider-wrap mb-3"><div class="label-container"><span>Fr - Froude Number (Velocity)</span><span id="v-fr">0.30</span></div><input type="range" class="form-range" id="fr" min="0.1" max="0.5" step="0.01" value="0.30" oninput="syncParams()"></div>
                </div>
            </div>

            <div class="col-lg-6">
                <div class="viz-container">
                    <canvas id="boatCanvas" style="width:100%; height:100%;"></canvas>
                    <div style="position: absolute; top: 10px; right: 15px; color: rgba(255,255,255,0.8); font-size: 0.6rem; font-weight: bold; text-transform: uppercase;">Side-View Wave Visualization</div>
                </div>
                <div class="module-card">
                    <div class="row text-center mb-3">
                        <div class="col-6"><p class="text-muted small mb-1">Output: Rr (kN)</p><h4 class="fw-bold" id="rr-out">--</h4></div>
                        <div class="col-6 border-start"><p class="text-muted small mb-1">Carbon (kg/h)</p><h4 class="fw-bold text-success" id="co2-out">--</h4></div>
                    </div>
                    <canvas id="liveChart" height="160"></canvas>
                </div>
            </div>

            <div class="col-lg-3">
                <div class="module-card">
                    <h6 class="fw-bold mb-3 border-start border-4 border-info ps-2">Decision Support</h6>
                    <canvas id="xaiChart" class="mb-3" height="150"></canvas>
                    <div class="decision-box" id="decision-text">
                        <span class="fw-bold small">Engineering Advice:</span><br>
                        <span id="recommendation-content" class="small">Waiting for telemetry...</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // --- Side-View Canvas Animation Logic ---
        const canvas = document.getElementById('boatCanvas');
        const ctx = canvas.getContext('2d');
        let waveOffset = 0; let curRr = 5; let curFr = 0.1;
        let active = false;

        function drawSideScene() {
            canvas.width = canvas.offsetWidth; canvas.height = canvas.offsetHeight;
            const centerY = canvas.height / 2 + 20;
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Movement tied to Froude Number
            if(active) waveOffset += (curFr * 8);

            // Wave Amplitude tied to Residuary Resistance (Rr)
            const amplitudeBase = active ? Math.max(curRr * 0.8, 3) : 3; 
            const amplitudeChoppy = amplitudeBase * 0.3;

            // Draw Ocean
            ctx.beginPath(); ctx.moveTo(0, canvas.height);
            for (let x = 0; x <= canvas.width; x += 5) {
                const y = centerY + Math.sin((x + waveOffset) * 0.02) * amplitudeBase + Math.sin((x + waveOffset*1.5) * 0.05) * amplitudeChoppy;
                ctx.lineTo(x, y);
            }
            ctx.lineTo(canvas.width, canvas.height); ctx.closePath();
            const waterGrad = ctx.createLinearGradient(0, centerY - 50, 0, canvas.height);
            waterGrad.addColorStop(0, '#1E90FF'); waterGrad.addColorStop(1, '#00008B');
            ctx.fillStyle = waterGrad; ctx.fill();
            ctx.strokeStyle = 'rgba(255,255,255,0.3)'; ctx.lineWidth = 2; ctx.stroke();

            // Bobbing Boat
            const boatX = canvas.width / 2;
            const boatYAtWater = centerY + Math.sin((boatX + waveOffset) * 0.02) * amplitudeBase + Math.sin((boatX + waveOffset*1.5) * 0.05) * amplitudeChoppy;
            
            ctx.fillStyle = '#e53e3e'; ctx.beginPath();
            ctx.moveTo(boatX-40, boatYAtWater-5); ctx.lineTo(boatX+50, boatYAtWater-5); ctx.lineTo(boatX+65, boatYAtWater-25); ctx.lineTo(boatX-45, boatYAtWater-25);
            ctx.closePath(); ctx.fill();
            ctx.fillStyle = '#2d3748'; ctx.fillRect(boatX-20, boatYAtWater-45, 30, 20);
            
            requestAnimationFrame(drawSideScene);
        }
        drawSideScene();

        // --- Charts and Data Pipeline ---
        const lCtx = document.getElementById('liveChart').getContext('2d');
        const liveChart = new Chart(lCtx, {
            type: 'line',
            data: { labels: [], datasets: [{ label: 'Rr', data: [], borderColor: '#3182ce', backgroundColor: 'rgba(49,130,206,0.1)', fill: true, tension: 0.4, pointRadius: 0 }] },
            options: { animation: false, scales: { x: { display: true, ticks: {font:{size:9}} }, y: { title: {display:true, text:'Rr (kN)', font:{size:10}} } }, plugins: { legend: { display: false } } }
        });

        const xCtx = document.getElementById('xaiChart').getContext('2d');
        new Chart(xCtx, {
            type: 'bar',
            data: { labels: ['Fr', 'PC', 'LC', 'LD', 'BDr', 'LB'], datasets: [{ data: [0.62, 0.18, 0.08, 0.06, 0.04, 0.02], backgroundColor: '#4299e1' }] },
            options: { indexAxis: 'y', plugins: { legend: { display: false } }, scales: { x: { display: false }, y: { ticks: { font: { size: 10 } } } } }
        });

        function syncParams() {
            const payload = { lc: parseFloat(document.getElementById('lc').value), pc: parseFloat(document.getElementById('pc').value), ld: parseFloat(document.getElementById('ld').value), bdr: parseFloat(document.getElementById('bdr').value), lb: parseFloat(document.getElementById('lb').value), fr: parseFloat(document.getElementById('fr').value) };
            for(let k in payload) document.getElementById('v-'+k).innerText = payload[k];
            fetch('/api/update_params', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload) })
                .then(r => r.json()).then(d => {
                    document.getElementById('rr-out').innerText = d.rr; document.getElementById('co2-out').innerText = d.carbon;
                    updateDecisionUI(d.recommendation);
                });
        }

        function toggleTelemetry() {
            fetch('/api/toggle_system', {method: 'POST'}).then(r => r.json()).then(d => {
                active = d.active; const btn = document.getElementById('mainBtn');
                btn.innerText = d.active ? "Stop Telemetry" : "Start Telemetry";
                btn.className = d.active ? "btn btn-danger btn-custom btn-sm" : "btn btn-outline-primary btn-custom btn-sm";
            });
        }

        function updateDecisionUI(msg) {
            const box = document.getElementById('decision-text'); const content = document.getElementById('recommendation-content');
            content.innerText = msg; box.classList.remove('highlight-red', 'highlight-yellow', 'highlight-green');
            if(msg.includes('CRITICAL')) box.classList.add('highlight-red');
            else if(msg.includes('CAUTION')) box.classList.add('highlight-yellow');
            else if(msg.includes('OPTIMAL') || msg.includes('STABLE')) box.classList.add('highlight-green');
        }

        setInterval(() => {
            fetch('/api/telemetry').then(r => r.json()).then(data => {
                if(data.length === 0) return; const latest = data[data.length - 1];
                liveChart.data.labels = data.map(i => i.time); liveChart.data.datasets[0].data = data.map(i => i.rr); liveChart.update();
                document.getElementById('rr-out').innerText = latest.rr; document.getElementById('co2-out').innerText = latest.carbon;
                document.getElementById('v-fr').innerText = latest.fr_val; curRr = latest.rr; curFr = latest.fr_val;
                updateDecisionUI(latest.recommendation);
            });
        }, 1000);
    </script>
</body>
</html>
"""

if __name__ == '__main__':
    # Using Port 5001 to avoid AirPlay conflict on macOS
    app.run(debug=True, port=5001, use_reloader=False)