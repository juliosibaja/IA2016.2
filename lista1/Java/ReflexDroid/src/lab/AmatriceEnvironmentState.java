package lab;

import java.util.LinkedHashMap;
import java.util.Map;

import aima.core.agent.Agent;
import aima.core.agent.EnvironmentState;
import lab.AmatriceEnviroment.LocationState;

public class AmatriceEnvironmentState implements EnvironmentState, FullyObservableAmatriceEnvironmentPercept, Cloneable {

	private Map<String, AmatriceEnviroment.LocationState> state;
	private Map<Agent, String> agentLocations;
	
	/**
	 * Constructor
	 */
	public AmatriceEnvironmentState() {
		state = new LinkedHashMap<String, AmatriceEnviroment.LocationState>();
		agentLocations = new LinkedHashMap<Agent, String>();
		initWorld();
	}

	private void initWorld() {
		// TODO Auto-generated method stub
		// Fill the AmatriceEnviroment specification
		// call the fill method bellow filling each stage
		
		// Example:
		// fill(LocationState.Human, LocationState.Rock, LocationState.Human);
		
		int n = 8; // put a random value here!
		this.state.clear();
		
		for (int i = 1; i < n; i++) {
			this.state.put(i + "", LocationState.None);
			
		}
		
		this.state.put((n -1) + "", LocationState.Human);
		
	}
	

	@Override
	public String getAgentLocation(Agent a) {
		return agentLocations.get(a);
	}

	/**
	 * Sets the agent location
	 * 
	 * @param a
	 * @param location
	 */
	public void setAgentLocation(Agent a, String location) {
		agentLocations.put(a, location);
	}

	@Override
	public AmatriceEnviroment.LocationState getLocationState(String location) {
		return state.get(location);
	}

	/**
	 * Sets the location state
	 * 
	 * @param location
	 * @param s
	 */
	public void setLocationState(String location, AmatriceEnviroment.LocationState s) {
		state.put(location, s);
	}

	@Override
	public boolean equals(Object obj) {
		if (getClass() == obj.getClass()) {
			AmatriceEnvironmentState s = (AmatriceEnvironmentState) obj;
			return state.equals(s.state) && agentLocations.equals(s.agentLocations);
		}
		return false;
	}

	/**
	 * Override hashCode()
	 * 
	 * @return the hash code for this object.
	 */
	@Override
	public int hashCode() {
		return 3 * state.hashCode() + 13 * agentLocations.hashCode();
	}

	@Override
	public AmatriceEnvironmentState clone() {
		AmatriceEnvironmentState result = null;
		try {
			result = (AmatriceEnvironmentState) super.clone();
			result.state = new LinkedHashMap<String, LocationState>(state);
			agentLocations = new LinkedHashMap<Agent, String>(agentLocations);
		} catch (Exception ex) {
			ex.printStackTrace();
		}
		return result;
	}
	
	/**
	 * Returns a string representation of the environment
	 * 
	 * @return a string representation of the environment
	 */
	@Override
	public String toString() {
		return this.state.toString();
	}

	public boolean isAgentAtHome(Agent agent) {
		// TODO Auto-generated method stub
		int actualLocation = Integer.parseInt(this.getAgentLocation(agent));
		return actualLocation == state.size();
	}

}
