document.addEventListener("DOMContentLoaded", function() {
    // 1. Get the canvas element
    const ctx = document.getElementById('trendChart').getContext('2d');

    // 2. Define the Chart Data (Placeholder for now)
    const chartConfig = {
        type: 'line',
        data: {
            labels: ['2021 Q1', '2021 Q2', '2021 Q3', '2021 Q4', '2022 Q1', '2022 Q2'],
            datasets: [
                {
                    label: 'Accidents',
                    data: [180, 210, 195, 205, 240, 245], // Fake data matching your image
                    borderColor: '#3B82F6', // Blue
                    backgroundColor: 'rgba(59, 130, 246, 0.1)',
                    tension: 0.4, // Smooth curves
                    fill: true
                },
                {
                    label: 'Injuries',
                    data: [200, 280, 260, 290, 360, 380], // Fake data
                    borderColor: '#F59E0B', // Orange
                    tension: 0.4,
                    borderDash: [5, 5], // Dashed line
                    fill: false
                },
                {
                    label: 'Fatalities',
                    data: [10, 15, 12, 18, 25, 20], // Fake data
                    borderColor: '#EF4444', // Red
                    tension: 0.4,
                    fill: false
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'bottom' }
            },
            scales: {
                y: { beginAtZero: true }
            }
        }
    };

    // 3. Create the Chart
    new Chart(ctx, chartConfig);
});