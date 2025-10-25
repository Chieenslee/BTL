from flask import Flask, render_template, request, jsonify
import json
import csv
import io
from tsp_solver import TSPBranchBoundSolver, Graph, create_sample_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/solve', methods=['POST'])
def solve_tsp():
    try:
        data = request.get_json()
        
        # Tạo đồ thị từ dữ liệu đầu vào
        graph = Graph()
        
        # Thêm các đỉnh (thành phố)
        cities = data.get('cities', [])
        for city in cities:
            graph.add_vertex(city['name'])
        
        # Thêm các cạnh (khoảng cách giữa các thành phố)
        distances = data.get('distances', [])
        for distance in distances:
            graph.add_edge(distance['from'], distance['to'], distance['weight'])
        
        # Giải bài toán TSP
        solver = TSPBranchBoundSolver(graph)
        result = solver.solve()
        
        return jsonify({
            'success': True,
            'route': result['route'],
            'total_distance': result['total_distance'],
            'execution_time': result['execution_time']
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if file and file.filename.endswith('.csv'):
            # Xử lý file CSV
            content = file.read().decode('utf-8')
            csv_reader = csv.DictReader(io.StringIO(content))
            
            cities = []
            distances = []
            
            for row in csv_reader:
                if 'city' in row:
                    cities.append({'name': row['city']})
                elif 'from' in row and 'to' in row and 'distance' in row:
                    distances.append({
                        'from': row['from'],
                        'to': row['to'],
                        'weight': float(row['distance'])
                    })
            
            return jsonify({
                'success': True,
                'cities': cities,
                'distances': distances
            })
        
        elif file and file.filename.endswith('.json'):
            # Xử lý file JSON
            content = file.read().decode('utf-8')
            data = json.loads(content)
            
            return jsonify({
                'success': True,
                'cities': data.get('cities', []),
                'distances': data.get('distances', [])
            })
        
        else:
            return jsonify({'error': 'Unsupported file format'}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/sample-data')
def get_sample_data():
    """API endpoint để lấy dữ liệu mẫu"""
    try:
        cities, distances = create_sample_data()
        return jsonify({
            'success': True,
            'cities': cities,
            'distances': distances
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
