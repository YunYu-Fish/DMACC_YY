/**
 * @author yunyu - yyu3@dmacc.edu
 * CIS175 - Fall 2021
 * Sep 20, 2023
 */
package model;

import javax.swing.Spring;

public class Employee {
	
	private String name;
	
	private double monthlySalary;
	
	private int age;
	
	// Default no-arg constructor
	public Employee() {
		
	}
	
	// Constructor that takes name and sets the name instance variable
	public Employee(String name) {
		this.name = name;
	}
	
	// Getter and Setter for name
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}

	// Getter and Setter for monthlySalary
	public double getMonthlySalary() {
		return monthlySalary;
	}
	public void setMonthlySalary(double monthlySalary) {
		this.monthlySalary = monthlySalary;
	}

	//Getter and Setter for age
	public Integer getAge() {
		return age;
	}
	public void setAge(Integer age) {
		this.age = age;
	}
	
	
}
