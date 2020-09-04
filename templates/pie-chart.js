{% block charts %}
    var myPieChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: {{data['countries_name']|safe}},
      datasets: [{
        data: {{data['countries_value']|safe}},
        backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc','#e74a3b','#5a5c69'],
        hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf','#e74a3d','#5a5c6d'],
        hoverBorderColor: "rgba(234, 236, 244, 1)",
      }],
    },
    options: {
      maintainAspectRatio: false,
      tooltips: {
        backgroundColor: "rgb(255,255,255)",
        bodyFontColor: "#858796",
        borderColor: '#dddfeb',
        borderWidth: 1,
        xPadding: 15,
        yPadding: 15,
        displayColors: false,
        caretPadding: 10,
      },
      legend: {
        display: true
      },
      // cutoutPercentage: 80,
      percentageInnerCutout: 20,
    },
  });
{% endblock %}