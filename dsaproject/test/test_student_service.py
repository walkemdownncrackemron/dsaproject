import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.services.student_service import StudentService
from src.models.student import Student

def test_student_service_crud():
    """Test basic CRUD operations in StudentService."""
    service = StudentService()
    
    # Test add student
    assert service.add_student("Alice", 20) == True
    assert service.add_student("Bob", 22) == True
    assert service.add_student("Charlie", 19, student_id=10) == True
    
    assert service.get_student_count() == 3
    
    # Test get student
    alice = service.get_student(1)
    assert alice is not None
    assert alice.name == "Alice"
    assert alice.age == 20
    
    charlie = service.get_student(10)
    assert charlie is not None
    assert charlie.name == "Charlie"
    
    # Test update student
    assert service.update_student(1, "Alice Smith", 21) == True
    updated_alice = service.get_student(1)
    assert updated_alice.name == "Alice Smith"
    assert updated_alice.age == 21
    
    # Test delete student
    assert service.delete_student(2) == True
    assert service.get_student(2) is None
    assert service.get_student_count() == 2
    
    # Test get all students
    all_students = service.get_all_students()
    assert len(all_students) == 2
    assert all_students[0].id == 1  # Should be sorted by ID
    assert all_students[1].id == 10
    
    print("Student service CRUD test passed!")

def test_student_service_search():
    """Test search functionality in StudentService."""
    service = StudentService()
    
    # Add test data
    service.add_student("Alice Johnson", 20)
    service.add_student("Bob Smith", 22)
    service.add_student("Alice Brown", 19)
    
    # Test search by name
    alice_students = service.search_students_by_name("Alice Johnson")
    assert len(alice_students) == 1
    assert alice_students[0].name == "Alice Johnson"
    
    # Test search with no results
    no_results = service.search_students_by_name("NonExistent")
    assert len(no_results) == 0
    
    # Test get min/max students
    min_student, max_student = service.get_min_max_students()
    assert min_student.id == 1
    assert max_student.id == 3
    
    print("Student service search test passed!")

def test_student_service_undo():
    """Test undo functionality in StudentService."""
    service = StudentService()
    
    # Add a student
    service.add_student("Alice", 20)
    assert service.get_student_count() == 1
    
    # Undo add
    assert service.undo_last_operation() == True
    assert service.get_student_count() == 0
    
    # Add student again (this time with specific ID to avoid ID conflicts)
    service.add_student("Bob", 22, student_id=1)
    bob = service.get_student(1)
    assert bob is not None
    
    # Update student
    service.update_student(1, "Bob Smith", 23)
    updated_bob = service.get_student(1)
    assert updated_bob.name == "Bob Smith"
    
    # Undo update
    assert service.undo_last_operation() == True
    restored_bob = service.get_student(1)
    assert restored_bob.name == "Bob"
    assert restored_bob.age == 22
    
    # Delete student
    service.delete_student(1)
    assert service.get_student(1) is None
    
    # Undo delete
    assert service.undo_last_operation() == True
    restored_bob = service.get_student(1)
    assert restored_bob is not None
    assert restored_bob.name == "Bob"
    
    print("Student service undo test passed!")

def test_student_service_statistics():
    """Test statistics functionality in StudentService."""
    service = StudentService()
    
    # Add some students
    service.add_student("Alice", 20)
    service.add_student("Bob", 22)
    service.add_student("Charlie", 19)
    
    # Test statistics
    stats = service.get_statistics()
    assert stats['total_students'] == 3
    assert stats['next_available_id'] == 4
    assert stats['min_student'].name == "Alice"
    assert stats['max_student'].name == "Charlie"
    
    # Test operation history
    history = service.get_operation_history()
    assert len(history) == 3  # 3 add operations
    assert "Add student ID 1 (Alice)" in history
    assert "Add student ID 2 (Bob)" in history
    assert "Add student ID 3 (Charlie)" in history
    
    print("Student service statistics test passed!")

def test_student_service_edge_cases():
    """Test edge cases and error handling."""
    service = StudentService()
    
    # Test get non-existent student
    assert service.get_student(999) is None
    
    # Test update non-existent student
    assert service.update_student(999, "Test") == False
    
    # Test delete non-existent student
    assert service.delete_student(999) == False
    
    # Test undo with no operations
    assert service.undo_last_operation() == False
    
    # Test duplicate ID
    service.add_student("Alice", 20, student_id=1)
    assert service.add_student("Bob", 22, student_id=1) == False
    
    # Test clear all data
    service.clear_all_data()
    assert service.get_student_count() == 0
    assert service.get_all_students() == []
    
    print("Student service edge cases test passed!")

def test_data_structure_integration():
    """Test integration between different data structures."""
    service = StudentService()
    
    # Add students
    service.add_student("Alice", 20)
    service.add_student("Bob", 22)
    service.add_student("Charlie", 19)
    
    # Test BST vs LinkedList ordering
    bst_order = service.get_all_students(sorted_by_id=True)
    linked_order = service.get_all_students(sorted_by_id=False)
    
    # BST should be sorted by ID
    assert bst_order[0].id == 1
    assert bst_order[1].id == 2
    assert bst_order[2].id == 3
    
    # LinkedList should be in insertion order
    assert linked_order[0].name == "Alice"
    assert linked_order[1].name == "Bob"
    assert linked_order[2].name == "Charlie"
    
    # Test that both structures have same data
    assert len(bst_order) == len(linked_order)
    
    # Test task processing
    pending_tasks = service.get_pending_tasks()
    assert len(pending_tasks) == 3  # 3 add operations queued
    
    # Process a task
    next_task = service.process_next_task()
    assert next_task is not None
    assert next_task['task_type'] == 'add'
    
    print("Data structure integration test passed!")

if __name__ == "__main__":
    test_student_service_crud()
    test_student_service_search()
    test_student_service_undo()
    test_student_service_statistics()
    test_student_service_edge_cases()
    test_data_structure_integration()
    print("\nAll StudentService tests passed!")
