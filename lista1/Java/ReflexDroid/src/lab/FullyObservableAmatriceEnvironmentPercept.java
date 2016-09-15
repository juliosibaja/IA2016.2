package lab;

import aima.core.agent.Agent;
import aima.core.agent.Percept;

public interface FullyObservableAmatriceEnvironmentPercept extends Percept {
	/**
	 * Returns the agent location
	 *
	 * @param a
	 * @return the agents location
	 */
	String getAgentLocation(Agent a);

	/**
	 * Returns the location state
	 *
	 * @param location
	 * @return the location state
	 */
	AmatriceEnviroment.LocationState getLocationState(String location);

}
