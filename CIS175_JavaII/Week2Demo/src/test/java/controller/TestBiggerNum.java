/**
 * @author yunyu - yyu3@dmacc.edu
 * CIS175 - Fall 2021
 * Sep 18, 2023
 */
package controller;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;


public class TestBiggerNum {
	
	biggerNum big = new biggerNum();

	@Test 
	public void TestBiggerNum() {
		assertTrue(big.biggerNum(10, 5));
		assertFalse(big.biggerNum(0, 1));
	}

}