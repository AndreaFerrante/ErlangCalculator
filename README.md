This Python package is an <i>helping hand</i> to all data analyst and scientist that are trying to determine scientifically how many call center agents to staff ! 🔥

The main teory under the hood has been developed in by Mr. Agner Krarup Erlang - who, back in the 1916, developed the concept of <i>Erlang Unit Measure</i> - and by Mr. Conny Palm - back in the 1946.

If we think about calls arriving into a call center we could think about their <i>distribution in time</i> like if it were a <i>Poisson Distribution</i>.
By having calls incoming flow one could assess how many agents are needed in order to answer the <i>Erlang measure of <b>offered load</b> (i.e. arriving calls !)</i>.

In this package I have developed a Python class that takes into reality different equations that compete together in defining correctly <i>how many agent to be staffed</i> given the amount of the incoming calls; this formulas are:

1. <b>Grade of Service (GoS)</b>: is the probability of a call in a circuit group being blocked or delayed for more than a specified interval
2. <b>ErlangC</b>: it is the equation to calculate delays or predict waiting times for callers
3. <b>ErlangB</b>: it is the probability that a customer arriving in a system with servers will be rejected because all the servers are busy
4. <b>ErlangA</b>: it is an extension to the ErlangC formula that takes into account the concept of <i>abandoned</i>

One important parameter that we must consider while modelling call center staff is the <i>shrinkage</i>: it is a ratio to model all that could get an agent away from answering to customer contacts. Industry shrinkage is 30%.

Long story short, here one example with assumptions:

- given the <b>AHT</b> (i.e. Average Handling Time or answering call duration), let's assume 250 seconds
- given the <b>TAT</b> (i.e. Targeting Answering Time which is the time before a call is supposed to be answered), let's assume 20 seconds
- given the <b>incoming call prediction</b>, for instance in one hour, let's assume 200 calls
- given a target <b>GoS</b>  to be achieved, let's assume 75%

we have that the number of agents that are supposed to be present are <i>18 (25.7 given the insustry shrinkage).</i>
Basically, as written in the Python code, one could stop the GoS and force the number of agents into the ErlangC formula that conctructs the GoS itself...

Different story is the <i>abandoned rate</i> which is the second parameter used in call centers to evaluate parformance: one could always get it fixed to assess the number of agents but, instead of focusing on the ErlangC equation, one should user the ErlangA equation.

For the curious reader and coder, here the two references from which the package has taken mathematical sources:

a. https://core.ac.uk/download/8987165.pdf \
b. https://iew3.technion.ac.il/serveng/References/MMNM_IAO.pdf

(a) point gives detailed and clear ErlangC and GoS equations, (b) point addresses ErlangA equation to get the abandoned rate into account: abandoned rate is nothing more than the relation between two probabilities (all Erlang stuff is a super funny probability model !) as shown at the very end of page 27. \
Mischievous reader can have identical results for the Erlang Call Center staffing model out of here:

I. https://www.callcentrehelper.com/tools/erlang-calculator/

Enjoy coding (Python !) and math !
