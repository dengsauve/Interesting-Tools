using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Bugger
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // For use in loop later
        bool started = false;

        // Collection of phrases for spamming :D
        string[] phrases = new string[]
        {
            "Hi",
            "What's up?",
            "I didn't hit her",
            "You don’t notice the air, until someone spoils it.",
            "Don’t drink while driving – you will spill the beer.",
            "If you love a woman, you shouldn’t be ashamed to show her to your wife.",
            "Life didn’t work out, but everything else is not that bad.",
            "If someone notices you with an open zipper, answer proudly: professional habit.",
            "If you’re not supposed to eat at night, why is there a light bulb in the refrigerator?",
            "FRIDAY is my second favorite F word.",
            "There is a new trend in our office; everyone is putting names on their food.I saw it today, while I was eating a sandwich named Kevin.",
            "The speed of light is when you take out a bottle of beer out of the fridge before the light comes on.",
            "To weigh 50 kilos and say that you’re fat, that is so female…",
            "I have been to many places but my goal is to go everywhere.",
            "If Mayans could predict the future, why didn’t they predict their extinction?",
            "Let's go!",
            "Are you sleeping?",
            "How you doing?",
            "I'm bothertron Riiiiiiiiiiick!",
            "I turned myself into a bothering computronic!",
            "O hi mark!"
        };

        private void Form1_Load(object sender, EventArgs e)
        {
            // Adding hover text to intervals for range information

            new ToolTip().SetToolTip(numericMinInterval, "Range: 250 - 600");
            new ToolTip().SetToolTip(numericMaxInterval, "Range: 650 - 3000");

            MessageBox.Show(
                "This Application was built in a Windows 10 Environment." +
                "\n\nI cannot and will not guarantee the stability of this program on any older operating systems." +
                "\nThis is due largely in part to not having access to Windows 7 or 8 machines to do any testing." +
                "\n\nI have witnessed this program fail spectacularly on Windows 7, freezing the entire machine." +
                "\n\nYou have been warned!",
                "Operating System Warning",
                MessageBoxButtons.OK,
                MessageBoxIcon.Hand
                );
        }

        private async void btnStart_Click(object sender, EventArgs e)
        {
            started = true;

            // so people don't try to mess with timing during operation
            numericMinInterval.Enabled = false;
            numericMaxInterval.Enabled = false;

            // Taking into account user variables
            int minTime = (int)numericMinInterval.Value;
            int maxTime = (int)numericMaxInterval.Value;

            var personName = txtName.Text;

            // Randomizes the timing of the messages, in an attempt to look human
            Random rand = new Random();
            
            // Awesome countdown
            for(int i = 3; i > 0; i = i - 1)
            {
                lblStatus.Text = i.ToString();
                await waitTime(1000);
            }

            lblStatus.Text = "Bothering";

            while (started)
            {
                SendKeys.Send(personName);
                SendKeys.Send("{ENTER}");
                await waitTime(rand.Next(minTime, maxTime));
                SendKeys.Send(phrases[rand.Next(0, phrases.Count())]);
                SendKeys.Send("{ENTER}");
                await waitTime(rand.Next(minTime, maxTime));
            }
        }

        async Task waitTime(int time)
        {
            await Task.Delay(time);
        }

        private void btnStop_Click(object sender, EventArgs e)
        {
            started = false;

            numericMinInterval.Enabled = true;
            numericMaxInterval.Enabled = true;

            lblStatus.Text = "Not Bothering";
        }

        private void btnQuit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void btnUsage_Click(object sender, EventArgs e)
        {
            // opens https://github.com/dengsauve/Interesting-Tools/blob/master/FastText/Bugger/README.MD in a web browser

            System.Diagnostics.Process.Start("https://github.com/dengsauve/Interesting-Tools/blob/master/FastText/Bugger/README.MD");
        }
    }
}
