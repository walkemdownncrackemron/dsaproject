# Data Structures & Algorithms Project - Student Management System

## Overview

This project implements a comprehensive student management system that demonstrates the practical use of various data structures for CRUD (Create, Read, Update, Delete) operations. Instead of relying on a traditional database, the system uses custom implementations of fundamental data structures to manage student data.

## Data Structures Used

### 1. **Binary Search Tree (BST)**
- **Purpose**: Primary storage for efficient student lookup by ID
- **Operations**: Insert, search, delete, in-order traversal
- **Time Complexity**: O(log n) average case for search/insert/delete
- **Use Case**: Quick student retrieval and maintaining sorted order by ID

### 2. **Linked List**
- **Purpose**: Maintains insertion order and supports name-based searching
- **Operations**: Insert at head/tail, search by ID/name, delete, update
- **Time Complexity**: O(n) for search, O(1) for insertion at head
- **Use Case**: Preserving student registration order and flexible searching

### 3. **Stack (with Undo functionality)**
- **Purpose**: Implements undo operations for all CRUD actions
- **Operations**: Push operation, pop for undo, peek
- **Time Complexity**: O(1) for all operations
- **Use Case**: Allowing users to undo recent changes

### 4. **Queue (Priority Queue)**
- **Purpose**: Manages task processing with priority-based execution
- **Operations**: Enqueue with priority, dequeue highest priority
- **Time Complexity**: O(n) for priority insertion, O(1) for dequeue
- **Use Case**: Processing student operations based on priority

## Project Structure

```
dsaproject/
├── src/
│   ├── models/
│   │   └── student.py          # Student data model
│   ├── datastructures/
│   │   ├── bst.py              # Binary Search Tree implementation
│   │   ├── linkedlist.py       # Linked List implementation
│   │   ├── stack.py            # Stack and UndoStack implementation
│   │   └── queue.py            # Queue and PriorityQueue implementation
│   ├── services/
│   │   └── student_service.py  # Service layer coordinating all data structures
│   ├── ui/
│   │   └── app.py              # Tkinter GUI application
│   └── db/
│       └── database.py         # Legacy database code (not used)
├── test/
│   ├── test_bst.py             # BST unit tests
│   ├── test_linkedlist.py      # Linked List unit tests
│   ├── test_stack.py           # Stack unit tests
│   ├── test_queue.py           # Queue unit tests
│   └── test_student_service.py # Integration tests
├── main.py                     # Main application entry point
├── requirements.txt            # Project dependencies
└── README.md                   # This file
```

## Features

### Core CRUD Operations
- **Create**: Add new students with auto-generated or custom IDs
- **Read**: Search students by ID (BST) or name (LinkedList)
- **Update**: Modify student information with full rollback support
- **Delete**: Remove students with undo capability

### Advanced Features
- **Undo System**: Revert any of the last 100 operations
- **Dual View Modes**: View students sorted by ID (BST) or insertion order (LinkedList)
- **Priority Task Processing**: Background task queue for operation management
- **Statistics Dashboard**: View data structure metrics and operation history
- **Search Capabilities**: Find students by exact name match
- **Data Validation**: Comprehensive input validation and error handling

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python main.py
```

### 4. Run Tests
```bash
# Run all tests
python -m pytest dsaproject/test/

# Run specific test files
python dsaproject/test/test_bst.py
python dsaproject/test/test_linkedlist.py
python dsaproject/test/test_stack.py
python dsaproject/test/test_queue.py
python dsaproject/test/test_student_service.py
```

## Usage Guide

### GUI Application
1. **Adding Students**: Enter name and age, optionally specify an ID
2. **Searching**: Use "Search by Name" for name-based queries
3. **Updating**: Select a student from the list, modify fields, click "Update"
4. **Deleting**: Select a student and click "Delete Student"
5. **Undo**: Click "Undo Last Operation" to revert changes
6. **View Modes**: Switch between BST (sorted) and LinkedList (insertion order) views

### Key Benefits of This Approach

1. **Educational Value**: Demonstrates real-world application of data structures
2. **Performance**: Each data structure is optimized for specific operations
3. **Flexibility**: Multiple ways to access and organize the same data
4. **Robustness**: Comprehensive error handling and data validation
5. **Extensibility**: Easy to add new data structures or operations

## Technical Implementation Details

### Student Model
- Immutable data class with validation
- Supports comparison operations for BST
- Includes comprehensive string representation

### Service Layer
- Coordinates all data structures
- Maintains data consistency across structures
- Handles complex operations like undo/redo
- Provides unified API for the UI

### Error Handling
- Graceful handling of invalid inputs
- Rollback mechanisms for failed operations
- User-friendly error messages
- Comprehensive logging

## Performance Characteristics

| Operation | BST | LinkedList | Stack | Queue |
|-----------|-----|------------|-------|-------|
| Search by ID | O(log n) | O(n) | N/A | N/A |
| Search by Name | N/A | O(n) | N/A | N/A |
| Insert | O(log n) | O(1) | O(1) | O(1) |
| Delete | O(log n) | O(n) | O(1) | O(1) |
| Undo | N/A | N/A | O(1) | N/A |


## Contributing

1. Fork the repository
2. Create a feature branch
3. Implement your changes with tests
4. Submit a pull request

## License

This project is for educational purposes as part of a Data Structures and Algorithms course.
