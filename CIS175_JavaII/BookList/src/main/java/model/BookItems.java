package model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

/**
 * yunyu - yyu3@dmacc.edu
 * CIS175 Fall 2023
 * Oct 4, 2023
 */

@Entity(name="book_items")
@Table(name="book_items")
public class BookItems {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int rowId;
	
	private String title;
	private String author;
	private int Year;
	
	// Getter and Setter
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getAuthor() {
		return author;
	}
	public void setAuthor(String author) {
		this.author = author;
	}
	public int getYear() {
		return Year;
	}
	public void setYear(int year) {
		Year = year;
	}
	
	public int getRowId() {
		return rowId;
	}
	public void setRowId(int rowId) {
		this.rowId = rowId;
	}
	
	public BookItems() {
		super();
	}
	
	public BookItems(String title, String author, int year) {
		super();
		this.title = title;
		this.author = author;
		Year = year;
	}
}
