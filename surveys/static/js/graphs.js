window.onload = (event) => {
  
  const bg_colours = ['rgb(17, 35, 90)','rgb(89, 111, 183)','rgb(82, 92, 235)','rgb(134, 182, 246)','rgb(23, 107, 135)','rgb(92, 131, 116)','rgb(158, 200, 185)','rgb(198, 207, 155)','rgb(246, 236, 169)']
  const graphs = document.getElementsByTagName('canvas');
  const graph_data =JSON.parse(document.getElementById('graph-data').textContent);

  let graph_number = 0;

  Object.values(graph_data).forEach(value => {
    let obj = value
    let values = Object.values(obj)
    let labels = Object.keys(obj)
    // console.log(data)
    // console.log(labels)

    const data = {
      labels: labels,
      datasets: [{
        data: values,
        backgroundColor: bg_colours,
        hoverOffset: 4,
      }]
    };
    const config = {
    type: 'doughnut',
    data: data,
    options: {
      plugins: {
          legend: {
              position: 'right',
          }
      }
  }
    };
    
    new Chart(graphs[graph_number], config);
    graph_number ++;
  })

  // console.log(graphs)
  // console.log(data)
  // const data = {
  //   labels: [
  //     'Red',
  //     'Blue',
  //     'Yellow'
  //   ],
  //   datasets: [{
  //     label: 'My First Dataset',
  //     data: [300, 50, 100],
  //     backgroundColor: [
  //       'rgb(255, 99, 132)',
  //       'rgb(54, 162, 235)',
  //       'rgb(255, 205, 86)'
  //     ],
  //     hoverOffset: 4
  //   }]
  // };

  // const config = {
  //   type: 'doughnut',
  //   data: data,
  // };

  // new Chart(document.getElementById('graph-1'), config);
};