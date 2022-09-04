import wx

from convertor import Convertor


class MainFrame(wx.Frame):
    def __init__(self, parent, id, title, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        self.set_properties()
        self.make_menu_bar()
        self.create_ctrls()
        self.bind_events()
        self.create_layout()
        self.convertor = Convertor()
        
        self.CenterOnScreen(wx.BOTH)
    
    def set_properties(self):
        """Sets the window icon and minimum, maximum and general size for the window."""
        self.SetIcon(wx.Icon("themometer.ico"))
        self.SetSize((450, 200))
        self.SetMinSize((450, 200))
        self.SetMaxSize((450, 200))
    
    def make_menu_bar(self):
        """"""
        menu_bar = wx.MenuBar()
        
        self.menu = wx.Menu()
        
        self.menu.Append(101, item="&Convert Temperatutres", helpString="Convert Temperatures")
        self.menu.AppendSeparator()
        self.menu.Append(102, item="&Reset", helpString="Reset")
        self.menu.AppendSeparator()
        self.menu.Append(103, item="&Close", helpString="Close")
        
        menu_bar.Append(self.menu, title="&Menu")
        
        self.SetMenuBar(menu_bar)
    
    def create_ctrls(self):
        """Creates the panel, labels, text inputs and buttons."""
        self.panel = wx.Panel(parent=self, id=-1, pos=wx.DefaultPosition, style=wx.BORDER_DEFAULT)
        self.panel.SetBackgroundColour(wx.WHITE)
        
        # Celcius Ctrls
        self.celcius_label = wx.StaticText(parent=self.panel, pos=wx.DefaultPosition, label="Celcius", style=wx.ALIGN_CENTER | wx.ST_NO_AUTORESIZE)
        
        self.celcius_input = wx.TextCtrl(parent=self.panel, id=wx.ID_ANY, value="", style=wx.TE_PROCESS_ENTER)
        
        # Fahrenheit Ctrls
        self.fahrenheit_label = wx.StaticText(parent=self.panel, pos=wx.DefaultPosition, label="Fahrenheit", style=wx.ALIGN_CENTER | wx.ST_NO_AUTORESIZE)
        
        self.fahrenheit_input = wx.TextCtrl(parent=self.panel, id=wx.ID_ANY, value="", style=wx.TE_PROCESS_ENTER)
        
        # Kelvin Ctrls
        self.kelvin_label = wx.StaticText(parent=self.panel, pos=wx.DefaultPosition, label="Kelvin", style=wx.ALIGN_CENTER | wx.ST_NO_AUTORESIZE)
        
        self.kelvin_input = wx.TextCtrl(parent=self.panel, id=wx.ID_ANY, value="", style=wx.TE_PROCESS_ENTER)
        
        # Reset / Convert Buttons
        self.btn_reset = wx.Button(self.panel, id=102, pos=wx.DefaultPosition, label="&Reset", size=wx.DefaultSize, style=0, name="reset_btn")
        
        self.btn_convert = wx.Button(self.panel, pos=wx.DefaultPosition, label="&Convert", size=wx.DefaultSize, style=0, name="convert_btn")
    
    def bind_events(self):
        """Event binds for buttons."""
        self.btn_reset.Bind(wx.EVT_BUTTON, self.reset_input_values)
        self.btn_convert.Bind(wx.EVT_BUTTON, self.convert_input_values)
        self.menu.Bind(wx.EVT_MENU, self.on_menu)
        self.celcius_input.Bind(wx.EVT_TEXT_ENTER, self.convert_input_values)
        self.fahrenheit_input.Bind(wx.EVT_TEXT_ENTER, self.convert_input_values)
        self.kelvin_input.Bind(wx.EVT_TEXT_ENTER, self.convert_input_values)
        
    def create_layout(self):
        """For the layout, creates sizers and adds labels, text inputs and sizers."""
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        temp_container_sizer = wx.BoxSizer(wx.HORIZONTAL)
        celcius_sizer = wx.BoxSizer(wx.VERTICAL)
        fahrenheit_sizer = wx.BoxSizer(wx.VERTICAL)
        kelvin_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Sizer for the buttons
        button_sizer.Add(self.btn_convert, proportion=1, flag=wx.ALIGN_CENTER, border=0)
        button_sizer.Add(self.btn_reset, proportion=1, flag=wx.ALIGN_CENTER, border=0)
        
        # Celcius Sizer
        celcius_sizer.Add(self.celcius_label, proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL, border=0)
        celcius_sizer.Add(self.celcius_input, proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL, border=0)
        
        # fahrenheit sizer
        fahrenheit_sizer.Add(self.fahrenheit_label, proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL, border=0)
        fahrenheit_sizer.Add(self.fahrenheit_input, proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL, border=0)
        
        # kelvin sizer
        kelvin_sizer.Add(self.kelvin_label, proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL, border=0)
        kelvin_sizer.Add(self.kelvin_input, proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL, border=0)
        
        # Sizer for the temperatuer inputs / labels
        temp_container_sizer.Add(celcius_sizer, proportion=1, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL, border=4)
        temp_container_sizer.Add(fahrenheit_sizer, proportion=1, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL, border=4)
        temp_container_sizer.Add(kelvin_sizer, proportion=1, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL, border=4)
        
        # Main sizer
        main_sizer.Add(button_sizer, proportion=1, flag=wx.ALIGN_CENTER, border=0)
        main_sizer.Add(temp_container_sizer, proportion=1, flag=wx.ALIGN_CENTER, border=0)
        
        self.panel.SetSizerAndFit(main_sizer)
    
    def on_menu(self, event, user_input=None):
        """Events for menu bar selections."""
        if event.GetId() == 101:
            self.convert_input_values(event, user_input)
        elif event.GetId() == 102:
            self.reset_input_values(event)
        elif event.GetId() == 103:
            self.on_close(event)
    
    def reset_input_values(self, event):
        """Resets the values in all TextCtrls to an empty string. Binds to Reset button and the reset option in menu."""
        
        reset_menu_id = event.GetId()
        
        button_id = event.GetId()
        button_by_id = self.FindWindowById(button_id)
        
        if button_by_id.GetName() == self.btn_reset.GetName() or reset_menu_id == 102:
            self.celcius_input.Clear()
            self.fahrenheit_input.Clear()
            self.kelvin_input.Clear()
    
    def convert_input_values(self, event, user_input=None):
        """Converts the value placed in designated temperature TextCtrl to 
        relevant temperatures, which are then entered as values in relevant 
        temperature TextCtrls.
        e.g. value (int / float) entered in celcius TextCtrl is then converted 
        in to fahrenheit and kelvin temperatures, these values are then entered 
        into the relevant TextCtrls.
        
        Binds to Convert button"""
        
        if self.celcius_input.GetValue() != "" and self.fahrenheit_input.GetValue() == "" and self.kelvin_input.GetValue() == "":
            self.convert_celsius_to_fahrenheit_and_kelvin(user_input)

        if self.fahrenheit_input.GetValue() != "" and self.celcius_input.GetValue() == "" and self.kelvin_input.GetValue() == "":
            self.convert_fahrenheit_to_celcius_and_kelvin(user_input)
        
        if self.kelvin_input.GetValue() != "" and self.celcius_input.GetValue() == "" and self.fahrenheit_input.GetValue() == "":
            self.convert_kelvin_to_celcius_and_fahrenheit(user_input)
    
    def convert_celsius_to_fahrenheit_and_kelvin(self, user_input):
        """"""
        try:
            self.fahrenheit_input.SetValue(f"{self.convertor.celsius_to_fahrenheit(self.celcius_input.GetValue())} °F")
            self.kelvin_input.SetValue(f"{self.convertor.celsius_to_kelvin(self.celcius_input.GetValue())} °K")
        except ValueError:
            self.celcius_input.SetValue("Please use numbers.")
        except TypeError:
            self.celcius_input.SetValue("Unsupported types.")
        else:
            self.celcius_input.SetValue(f"{self.celcius_input.GetValue()} °C")
    
    def convert_fahrenheit_to_celcius_and_kelvin(self, user_input):
        """"""
        try:
            self.celcius_input.SetValue(f"{self.convertor.fahrenheit_to_celsius(self.fahrenheit_input.GetValue())} °C")
            self.kelvin_input.SetValue(f"{self.convertor.fahrenheit_to_kelvin(self.fahrenheit_input.GetValue())} °K")
        except ValueError:
            self.fahrenheit_input.SetValue("Please use numbers.")
        except TypeError:
            self.fahrenheit_input.SetValue("Unsupported types.")
        else:
            self.fahrenheit_input.SetValue(f"{self.fahrenheit_input.GetValue()} °F")
    
    def convert_kelvin_to_celcius_and_fahrenheit(self, user_input):
        """"""
        try:
            self.celcius_input.SetValue(f"{self.convertor.kelvin_to_celsius(self.kelvin_input.GetValue())} °C")
            self.fahrenheit_input.SetValue(f"{self.convertor.kelvin_to_fahrenheit(self.kelvin_input.GetValue())} °F")
        except ValueError:
            self.kelvin_input.SetValue("Please use numbers.")
        except TypeError:
            self.kelvin_input.SetValue("Unsupported types.")
        else:
            self.kelvin_input.SetValue(f"{self.kelvin_input.GetValue()} °K")
    
    def on_close(self, event):
        """Event for closure of app."""
        self.Close()


class ConvertorApp(wx.App):
    def OnInit(self):
        frame = MainFrame(parent=None, id=-1, title="Temperature Convertor")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

def main():
    app = ConvertorApp(redirect=False)
    app.MainLoop()

if __name__ == "__main__" :
    main() 
