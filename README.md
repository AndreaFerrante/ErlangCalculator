This Python package is an <i>helping hand</i> to all data analyst and scientist that are trying to assess scientifically how many call center agents to staff ! 🔥

The main teory under the hood has been developed in by Mr. Agner Krarup Erlang - who, back in the 1916, developed the concept of <i>Erlang Unit Measure</i> - and by Mr. Conny Palm - back in the 1946.

If we think about calls arriving into a call center we could think about their <i>distribution in time</i> like if it were a <i>Poisson Distribution</i>.
By having calls incoming flow one could assess how many agents are needed in order to answer the <i>Erlang measure of <b>offered load</b> (i.e. arriving calls !)</i>.

In this package I have developed a Python class that takes into reality different equations that compete together in defining correctly <i>how many agent to be staffed</i> given the amount of the incoming calls; this formulas are:

1. Grade of Service: is the probability of a call in a circuit group being blocked or delayed for more than a specified interval
2. ErlangC: it is the equation to calculate delays or predict waiting times for callers (developed by Mr. Erlang !)
3. ErlangB: it is the probability that a customer arriving in a system with servers will be rejected because all the servers are busy (developed by Mr. Erlang !)
4. ErlangA: it is an extension to the ErlangC formula that takes into account the concept of <i>abandoned</i> (developed by Mr. Palm !)

One note: in order to get a correct ErlangA, one should be looking at the Gamma Function
