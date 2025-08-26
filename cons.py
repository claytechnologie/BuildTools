class ConsoleEditor:
    
    def __init__(self):
        import rich
        self.rich = rich
        self.message = ""

    def error(self, message):
        self.message = message
        self.rich.print(f"[bold red]Error:[/bold red] {self.message}")
        
    def info(self, message):
        self.message = message
        self.rich.print(f"[bold yellow]Info:[/bold yellow] {self.message}")

    def success(self, message):
        self.message = message
        self.rich.print(f"[bold green]Success:[/bold green] {self.message}")

    def warning(self, message):
        self.message = message
        self.rich.print(f"[bold orange]Warning:[/bold orange] {self.message}")
    
    def debug(self, message):
        self.message = message
        self.rich.print(f"[bold magenta]Debug:[/bold magenta] {self.message}")
        
    def create(self, **parts):
        for i in parts.items():
            headline = i.get("text", "")
            text = i.get("text", "")
            color_headline = i.get("color", "")
            color_text = i.get("color", "")
            self.rich.print(f"[{color_headline}]{headline}[/{color_headline}] [{color_text}]{text}[/{color_text}]")
            
    def blue(self, message):
        self.message = message
        self.rich.print(f"[bold blue]{self.message}[/bold blue]")

    def cyan(self, message):
        self.message = message
        self.rich.print(f"[bold cyan]{self.message}[/bold cyan]")

    def green(self, message):
        self.message = message
        self.rich.print(f"[bold green]{self.message}[/bold green]")

    def yellow(self, message):
        self.message = message
        self.rich.print(f"[bold yellow]{self.message}[/bold yellow]")

    def orange(self, message):
        self.message = message
        self.rich.print(f"[bold orange]{self.message}[/bold orange]")

    def red(self, message):
        self.message = message
        self.rich.print(f"[bold red]{self.message}[/bold red]")

    def magenta(self, message):
        self.message = message
        self.rich.print(f"[bold magenta]{self.message}[/bold magenta]")

    def blue(self, message):
        self.message = message
        self.rich.print(f"[bold blue]{self.message}[/bold blue]")
