%Name: CoronaSimData
%This program analyzes the data for the 1 million trial simulation
%The simulation was conducted in RandomSim.py

data = readtable('ValRange');
T = data(:,2);

iterations = 1000000;

values_T = table2array(T);
values = values_T.';
values = sort(values);
values(70)

minimum = values(1);
maximum = values(iterations);

t = 1:1:iterations;
t1 = minimum:1:maximum;

figure(1)
plot(t, values);
title(sprintf('Distribution of Sorted MSQE for n = %d', iterations));
xlabel("MSQE")
ylabel("Trial")

histogram(values)
xlabel("MSE");
ylabel("Number of Trials");
title('Histogram of MSE Distribution for 1 Million Iterations');

