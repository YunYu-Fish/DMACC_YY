package controller;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

import model.BookItems;

/**
 * yunyu - yyu3@dmacc.edu
 * CIS175 Fall 2023
 * Oct 4, 2023
 */
public class BookListHelper {
	EntityManagerFactory factory = Persistence.createEntityManagerFactory("Book");
	
	public void persist(BookItems model) {
		EntityManager manager = factory.createEntityManager();
		manager.getTransaction().begin();
		manager.persist(model);
		manager.getTransaction().commit();
		manager.close();
	}
	
	public void delete (BookItems model) {
		EntityManager manager = factory.createEntityManager();
		manager.getTransaction().begin();
		manager.remove(manager.find(BookItems.class, model.getRowId()));
		manager.getTransaction().commit();
		manager.close();
	}
	
	@SuppressWarnings("unchecked")
	public List<BookItems> showAllBooks(){
		EntityManager manager = factory.createEntityManager();
		List<BookItems> allItems = manager.createQuery("SELECT b FROM book_items b").getResultList();
		manager.close();
		return allItems;
	}
	
	public void update (BookItems model) {
		EntityManager manager = factory.createEntityManager();
		BookItems dbEntity = manager.find(BookItems.class, model.getRowId());
		manager.getTransaction().begin();
		dbEntity.setTitle(model.getTitle());
		dbEntity.setAuthor(model.getAuthor());
		dbEntity.setYear(model.getYear());
		manager.getTransaction().commit();
		manager.close();
	}
}

