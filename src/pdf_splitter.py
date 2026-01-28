"""PDF Splitter Application
A simple GUI application to split PDF files into multiple documents.
"""

import os
import sys
import math
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PyPDF2 import PdfReader, PdfWriter


class PDFSplitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Splitter")
        self.root.geometry("600x480")
        self.root.resizable(False, False)
        icon_path = os.path.join(os.path.dirname(__file__), '../assets/icon.png')
        self.root.iconphoto(True, tk.PhotoImage(file=icon_path))
        
        self.selected_file = None
        self.output_dir = None
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="PDF Splitter", 
            font=("Arial", 18, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, sticky=tk.W, padx=0, pady=(0, 30))
        
        # File selection section
        file_frame = ttk.LabelFrame(main_frame, text="Select PDF File", padding="5")
        file_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        self.file_label = ttk.Label(file_frame, text="No file selected", foreground="gray")
        self.file_label.grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        
        select_btn = ttk.Button(file_frame, text="Browse...", command=self.select_file)
        select_btn.grid(row=0, column=1)
        
        # Output directory section
        output_frame = ttk.LabelFrame(main_frame, text="Output Directory", padding="5")
        output_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        self.output_label = ttk.Label(output_frame, text="Same as input file", foreground="gray")
        self.output_label.grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        
        output_btn = ttk.Button(output_frame, text="Change...", command=self.select_output_dir)
        output_btn.grid(row=0, column=1)
        
        # Pages per document section
        pages_frame = ttk.LabelFrame(main_frame, text="Pages per Document", padding="5")
        pages_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        pages_label = ttk.Label(pages_frame, text="Number of pages per output file:")
        pages_label.grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        
        self.pages_per_doc = tk.StringVar(value="3")
        pages_entry = ttk.Entry(pages_frame, textvariable=self.pages_per_doc, width=10)
        pages_entry.grid(row=0, column=1)
        
        # Progress section
        progress_frame = ttk.Frame(main_frame)
        progress_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=20)
        
        self.progress = ttk.Progressbar(progress_frame, mode='determinate')
        self.progress.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.status_label = ttk.Label(progress_frame, text="Ready", foreground="blue")
        self.status_label.grid(row=1, column=0, columnspan=2)
        
        # Split button
        split_btn = ttk.Button(
            main_frame, 
            text="Split PDF", 
            command=self.split_pdf,
            style="Accent.TButton"
        )
        split_btn.grid(row=5, column=0, columnspan=2, pady=(0, 10))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        progress_frame.columnconfigure(0, weight=1)
    
    def select_file(self):
        """Open file dialog to select PDF file"""
        filename = filedialog.askopenfilename(
            title="Select PDF file",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        if filename:
            self.selected_file = filename
            # Truncate long filenames for display
            display_name = Path(filename).name
            if len(display_name) > 50:
                display_name = display_name[:47] + "..."
            self.file_label.config(text=display_name, foreground="black")
            
            # Reset output directory to default
            if self.output_dir is None:
                self.output_label.config(text="Same as input file", foreground="gray")
    
    def select_output_dir(self):
        """Open directory dialog to select output directory"""
        directory = filedialog.askdirectory(title="Select output directory")
        
        if directory:
            self.output_dir = directory
            display_name = Path(directory).name
            if len(display_name) > 50:
                display_name = display_name[:47] + "..."
            self.output_label.config(text=display_name, foreground="black")
    
    def split_pdf(self):
        """Split the selected PDF into documents with specified pages"""
        if not self.selected_file:
            messagebox.showwarning("No File", "Please select a PDF file first.")
            return
        
        if not os.path.exists(self.selected_file):
            messagebox.showerror("Error", "Selected file does not exist.")
            return
        
        # Validate pages per document input
        try:
            pages_per_doc = int(self.pages_per_doc.get())
            if pages_per_doc < 1:
                raise ValueError("Must be at least 1")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of pages per document (must be a positive integer).")
            return
        
        try:
            # Determine output directory
            if self.output_dir:
                output_folder = self.output_dir
            else:
                output_folder = os.path.dirname(self.selected_file)
            
            # Create subfolder for split pages
            input_filename = Path(self.selected_file).stem
            output_folder = os.path.join(output_folder, f"{input_filename}_split")
            os.makedirs(output_folder, exist_ok=True)
            
            # Read the PDF
            self.status_label.config(text="Reading PDF...", foreground="blue")
            self.root.update()
            
            pdf_reader = PdfReader(self.selected_file)
            total_pages = len(pdf_reader.pages)
            
            if total_pages == 0:
                messagebox.showwarning("Empty PDF", "The selected PDF has no pages.")
                return
            
            # Calculate number of output documents
            total_docs = math.ceil(total_pages / pages_per_doc)
            
            # Set progress maximum to total pages
            self.progress['maximum'] = total_pages
            
            # Split into documents
            doc_num = 1
            page_idx = 0
            
            while page_idx < total_pages:
                pdf_writer = PdfWriter()
                
                # Add pages to this document
                pages_in_doc = min(pages_per_doc, total_pages - page_idx)
                for i in range(pages_in_doc):
                    pdf_writer.add_page(pdf_reader.pages[page_idx])
                    page_idx += 1
                    
                    # Update progress
                    self.progress['value'] = page_idx
                    self.status_label.config(
                        text=f"Processing page {page_idx} of {total_pages} (Document {doc_num}/{total_docs})...",
                        foreground="blue"
                    )
                    self.root.update()
                
                # Create output filename
                output_filename = os.path.join(
                    output_folder,
                    f"{input_filename}_part{doc_num}.pdf"
                )
                
                with open(output_filename, 'wb') as output_file:
                    pdf_writer.write(output_file)
                
                doc_num += 1
            
            # Success
            self.status_label.config(
                text=f"Success! Created {total_docs} document(s) from {total_pages} pages.",
                foreground="green"
            )
            self.progress['value'] = 0
            
            messagebox.showinfo(
                "Success",
                f"PDF split successfully!\n\n"
                f"Total pages: {total_pages}\n"
                f"Pages per document: {pages_per_doc}\n"
                f"Output documents: {total_docs}\n"
                f"Output location:\n{output_folder}"
            )
            
            # Open output folder
            if sys.platform == 'darwin':  # macOS
                os.system(f'open "{output_folder}"')
            elif sys.platform == 'win32':  # Windows
                os.startfile(output_folder)
            
        except Exception as e:
            self.progress['value'] = 0
            self.status_label.config(text="Error occurred", foreground="red")
            messagebox.showerror("Error", f"An error occurred:\n\n{str(e)}")


def main():
    """Launch the PDF Splitter application"""
    root = tk.Tk()
    app = PDFSplitterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()