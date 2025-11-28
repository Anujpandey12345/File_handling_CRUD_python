# 📁 File Manager CLI

A simple yet powerful command-line interface (CLI) application for managing files in your current directory. Perform CRUD (Create, Read, Update, Delete) operations on files with an intuitive menu-driven interface.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- **Create Files**: Create new files with custom content
- **Read Files**: View the contents of existing files
- **Update Files**: Modify files by renaming, overwriting, or appending content
- **Delete Files**: Remove files from your directory
- **Directory Overview**: View all files and folders in the current directory before performing operations

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher

### Installation

1. Clone or download the repository
2. Navigate to the project directory
3. Run the script:

```bash
python main.py
```

## 💡 How It Works

The application uses Python's `pathlib` module for modern file path handling and provides a simple menu-driven interface for file operations.

### Core Functionality

#### 1. **ReadFileandFolder()**
- Recursively scans and displays all files and folders in the current directory
- Uses `Path.rglob('*')` to enumerate all items
- Displays numbered list of all items for easy reference

#### 2. **createfile()**
- Creates a new file with user-specified name
- Checks if file already exists to prevent overwriting
- Allows immediate content input during creation
- Provides success/error feedback

#### 3. **readfile()**
- Reads and displays content of existing files
- Validates file existence before attempting to read
- Shows complete file content in the terminal

#### 4. **updatefile()**
- Offers three update options:
  - **Rename**: Change the file name
  - **Overwrite**: Replace entire file content
  - **Append**: Add new content to existing file
- Interactive menu for choosing update type

#### 5. **deletefile()**
- Safely removes files from the directory
- Validates file existence before deletion
- Provides confirmation of deletion

## 📖 Usage

When you run the script, you'll see the main menu:

```
Press 1 for Creating a file
Press 2 for Reading a file
Press 3 for Updating a file
Press 4 for Deleting a file
```

### Example Workflow

**Creating a File:**
```
Please tell your response: 1
Please tell your file name: example.txt
What you want to write in this file: Hello, World!
FILE CREATED SUCCESSFULLY
```

**Reading a File:**
```
Please tell your response: 2
Which file you want to read: example.txt
Hello, World!
Readed successfully
```

**Updating a File:**
```
Please tell your response: 3
tell me which file you want to update: example.txt
Press 1 for changing the name of your file
Press 2 for overwriting the data of your file
Press 3 for appending some content in your file
tell your response: 3
tell what you want to append: This is additional content.
```

**Deleting a File:**
```
Please tell your response: 4
tell me which file you want to delete: example.txt
File removed successfully
```

## 🛠️ Technical Details

### Key Python Modules Used

- **`pathlib.Path`**: Modern, object-oriented file system path handling
- **`os`**: Operating system interface for file operations
- **Built-in file handling**: `open()`, `read()`, `write()`, etc.

### Error Handling

The application includes comprehensive error handling:
- Try-except blocks in all major functions
- Existence checks before file operations
- User-friendly error messages

## 📝 Code Structure

```
main.py
├── ReadFileandFolder()    # Display directory contents
├── createfile()           # Create new file
├── readfile()             # Read file contents
├── updatefile()           # Update file (rename/overwrite/append)
├── deletefile()           # Delete file
└── Main Menu Logic        # User interface
```

## ⚠️ Important Notes

- The script operates in the **current working directory**
- Always check the file list before performing operations
- Be careful with delete and overwrite operations (they cannot be undone)
- File names should include extensions (e.g., `example.txt`, `data.json`)

## 🔮 Future Enhancements

- Add folder creation and deletion
- Support for binary files
- File search functionality
- Undo operations
- Configuration file support
- Colorized terminal output

## 👨‍💻 Author

**Anuj Kumar**

- 📧 Email: [anuj.a87a@gmail.com](mailto:anuj.a87a@gmail.com)
- 🌐 Portfolio: [https://anujcom.vercel.app/](https://anujcom.vercel.app/)
- 💼 LinkedIn: [Connect with me](https://www.linkedin.com/in/connectanujkumar/)
- 🚀 Projects: [View my work](https://anujcom.vercel.app/#portfolio)

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or reach out directly.

---

⭐ If you found this project helpful, please consider giving it a star!

**Happy Coding!** 💻