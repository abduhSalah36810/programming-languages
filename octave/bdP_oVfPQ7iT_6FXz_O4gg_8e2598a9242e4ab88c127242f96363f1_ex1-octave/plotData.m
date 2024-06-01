  data = load('ex1data1.txt');

  x = data(: , 1 ) ;
  y = data(: , 2 ) ;
  m = length(y) ;

  plot(x, y, 'rx', 'MarkerSize', 10); % Plot the data
  ylabel('Profit in $10,000s'); % Set the y−axis label
  xlabel('Population of City in 10,000s');
  xlim([4 , 26]);
  ylim([-5  , 25`]);
