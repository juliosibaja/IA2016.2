package lab;

import aima.core.agent.Agent;
import aima.core.agent.Environment;
import aima.core.agent.EnvironmentView;
import aima.core.agent.impl.SimpleEnvironmentView;

/**
 * Demonstrates, how to set up a simple environment, place an agent in it,
 * and run it. The vacuum world is used as a simple example.
 * 
 * @author Saulo Oliveira
 */
public class AmatriceProg {
	
	public static void main(String[] args) {

		Environment env = new AmatriceEnviroment();
		EnvironmentView view = new SimpleEnvironmentView();
		env.addEnvironmentView(view);
		
		Agent agent = new ReflexDroid();
		
		env.addAgent(agent);
		
		env.step(10);
		env.notifyViews("Performance=" + env.getPerformanceMeasure(agent));
	}
}
