package controller;

import java.util.Scanner;

import model.BookItems;

/**
 * yunyu - yyu3@dmacc.edu
 * CIS175 Fall 2023
 * Oct 4, 2023
 */
public class BookDriver {
	BookListHelper helper = new BookListHelper();
	
	public static void main(String[] args) {
		BookDriver run = new BookDriver();
		run.go();
	}
	
	private void go() {
		int userIn = 0;
		Scanner in = new Scanner(System.in);
		
		while(userIn !=5 ) {
			printMenu();
			userIn = in.nextInt();
			if(userIn == 1) {
				BookItems b = new BookItems();
				System.out.println("Enter the title of the book: ");
				b.setTitle(in.next());
				System.out.println("Enter the author of the book: ");
				b.setAuthor(in.next());
				System.out.println("Enter the publish year of the book: ");
				b.setYear(in.nextInt());
				helper.persist(b);
			}else if (userIn == 2) {
				showAll();
			}else if (userIn == 3) {
				BookItems b = new BookItems();
				System.out.println("Enter the Row ID of the book to delete: ");
				b.setRowId(in.nextInt());
				helper.delete(b);
			}else if (userIn == 4) {
				BookItems b = new BookItems();
				showAll();
				System.out.println("Enter the Row ID of the book to update: ");
				b.setRowId(in.nextInt());
				System.out.println("Enter the new title of the book: ");
				b.setTitle(in.next());
				System.out.println("Enter the new author of the book: ");
				b.setAuthor(in.next());
				System.out.println("Enter the new year of the book: ");
				b.setYear(in.nextInt());
				helper.update(b);
			}
		}
		System.out.println("Done!");
	}
	
	private void showAll() {
		for (BookItems b : helper.showAllBooks()) {
			System.out.println(b.toString());
		}
	}
	
	private void printMenu() {
		System.out.println("1.Create Book");
		System.out.println("2.Show Book");
		System.out.println("3.Delete Book");
		System.out.println("4.Update Book");
		System.out.println("5.Quit");
		System.out.println("**************");
	}
}
