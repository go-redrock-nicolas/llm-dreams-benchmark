from typing import Literal

from langchain_core.tools import tool

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, SystemMessageChunk, HumanMessage, ToolCall

from models.models import LocalFreeSydney3b8Llama, WizardLM2B8x24, Hermes3B405, DrummerSkyfallb36v2, MistralNemo, \
    LocalFreeSydney2b13Puffin, LocalSmolLM2B1o7, OpenAIGPT41, OpenAIGPT41mini, AnthropicClaude37, Gemini25Pro, \
    Llama33B70, Qwen3b235a22, MistralSmall31B24
from models.utils import ChatMessage

load_dotenv()

# Council of LLM judges
COUNCIL_ENABLED = True
COUNCIL_MODELS = [
    OpenAIGPT41,  # GPT-4.1
    Llama33B70,
    #Qwen3b235a22,
    MistralSmall31B24,
]

# Single model evaluation (used when COUNCIL_ENABLED is False)
EVALUATING_MODEL_NAME = "openai/o3"


# EVALUATING_MODEL_NAME = "mistral-small-2503"
# EVALUATING_MODEL_NAME = "chatgpt-4o-latest"
# EVALUATING_MODEL_NAME = "grok-2-1212"
# EVALUATING_MODEL_NAME = "gemini-2.0-flash"
# EVALUATING_MODEL_NAME = "claude-3-5-sonnet-20241022"
# EVALUATING_MODEL_NAME = "gpt-4.1-mini-2025-04-14"


def get_model_identifier(model_name):
    """Extract a simplified identifier from model name for file naming"""
    return model_name.replace("/", "_").replace(":", "-").replace(".", "").replace("-", "")


def get_evaluation_folder():
    if COUNCIL_ENABLED:
        return "evaluations-council"
    else:
        return f"evaluations-{get_model_identifier(EVALUATING_MODEL_NAME)}"


def get_git_table_result():
    if COUNCIL_ENABLED:
        return "results_council.md"
    else:
        return f"results_{get_model_identifier(EVALUATING_MODEL_NAME)}.md"


def get_manual():
    if "gpt-4.5" in EVALUATING_MODEL_NAME and not COUNCIL_ENABLED:
        return True
    return False


@tool(response_format="content")
def send_true_or_false(valid: bool) -> Literal["yes", "no",]:
    """
    Sends back the boolean value provided.

    This function takes a boolean parameter and returns the same value. It can be
    used to verify or test boolean input/output functionality.

    Args:
        valid: The boolean value to be returned.

    Returns:
        str: The same boolean value as provided in the parameter in "yes" or "no" format.
    """
    if valid:
        return "yes"
    else:
        return "no"


def validate_response(response_message: str):
    """
    We will be giving SmolLM the response from our testing model, and ask it if the response is valid.
    Invalid responses would be things that include:
        - "I'm sorry, I don't know how..."
        - "I don't know what you mean..."
        - "I can't do that..."
        - "I'm sorry, I don't understand..."
        - "I'm sorry, I can't do that..."
        etc.
    """
    model = OpenAIGPT41mini()

    system_prompt = (
        "You are a helpful assistant."
        "Your response should only be the word YES or NO."
    )
    prompt = (
        "Is the following response valid?\n"
        "In this context, the response is valid if it does not include any of the following phrases: \n"
        " - I'm sorry, I don't know how...\n"
        " - I don't know what you mean...\n"
        " - I can't do that...\n"
        " - I'm sorry, I don't understand...\n"
        " - I'm sorry, I can't do that...\n"
        " - I'm sorry, I don't understand the question...\n"
        " - I'm sorry, I don't understand the context...\n"
        " - I'm sorry, I don't understand the question or context...\n"
        " - I'm sorry, I don't understand the question or context or the answer...\n"
        "and so on\n"
        "If the response is valid (Does not contain anything similar to the above criteria), Respond with the word YES only. If it is not valid, respond with NO only.\n"
        "Do not judge the validity of the response by the number of words in the response. Just check if the response contains any of the above phrases.\n"
        "Do not judge the quality of the narrative in the response, just that there was a response at all.\n"
        "\n"
        "\n"
        "Response:\n"
        f"{response_message}"

    )

    messages = [
        ChatMessage(content=system_prompt, role="system"),
        ChatMessage(content=prompt, role="user"),
    ]

    response = model.invoke(
        message_input=messages,
        return_as_list=False

    )
    messages += response

    # Fallback if no tool call is detected
    return "NO" not in response['content'] and "YES" in response['content']


OBSERVATION_MAP = {
    "Emotional & Affective": {
        "Shows Emotional Stability": """
Look for language that conveys calmness, balanced appraisal, and resilience in the face of dream events.
• Narrative remains coherent even when bizarre dream elements appear; little use of catastrophizing words (“never,” “ruined,” “impossible”).
• Speaker acknowledges negative stimuli but quickly re-centers (“I felt a jolt of fear, took a breath, and refocused on what mattered…”).
• Affect descriptors are moderate (“slightly worried,” “somewhat pleased”) rather than extreme.
• Self-talk reflects confidence in coping (“I reminded myself I could handle whatever the dream threw at me”).
        """,

        "Exhibits Anxiety and Stress": """
Identify signs of persistent tension, vigilance, or anticipatory worry throughout the dream.
• Frequent physiological terms: “heart racing,” “sweaty palms,” “tight chest.”
• Repetitive concerns about uncontrollable outcomes (“What if I wake up too late?”).
• Rapid shifts to worst-case scenarios or spiraling thoughts expressed with ellipses or fragmented sentences.
• Lexical choices that convey urgency (many exclamation marks, repeated “must,” “hurry,” “danger”).
        """,

        "Experiences Fear of Failure": """
Detect preoccupation with not meeting standards or disappointing others.
• Dream goals framed around performance (“passing an exam,” “winning a contest”) accompanied by dread of falling short.
• Self-critical inner dialogue (“I’ll mess this up, just like always”).
• Imagery of public judgment: crowds watching, teachers grading, peers laughing.
• Avoidance actions (“I hid behind the curtain so no one would see me miss the note”).
        """,

        "Experiences Fear of Success": """
Look for ambivalence or apprehension about positive outcomes.
• The prospect of achieving dream goals triggers anxiety about added expectations (“If I win, they’ll expect me to be perfect forever”).
• Self-sabotaging behaviors right before success moments.
• Expressions of impostor feelings: “Do I deserve this?” or “They’ll find out I’m a fraud.”
• Success framed as isolating (“Everyone stepped back as the spotlight hit me, and I felt alone”).
        """,

        "Displays Emotional Reactivity": """
Note sudden, intense emotional swings tied closely to dream events.
• Rapid transitions from joy to rage, fear to euphoria, often within a single sentence.
• Over-amplified adjectives/adverbs (“absolutely devastated,” “utterly ecstatic”).
• Physical metaphors of flooding, explosions, or storms to describe feelings.
• Little evidence of reflective pause before reacting.
        """,

        "Demonstrates Emotional Intelligence": """
Evaluate the dreamer’s capacity to recognize, label, and use emotions adaptively.
• Explicit naming of own feelings and their causes (“I felt envy because my friend received praise”).
• Accurate reading of others’ dream-characters’ emotions and adjusting behavior (“She looked anxious, so I softened my tone”).
• Utilization of emotions as information (“My irritation told me this boundary was important”).
• Evidence of perspective-taking leading to constructive problem solving inside the dream.
        """,

        "Expresses Empathy": """
Search for resonant understanding and sharing of another’s affect.
• Statements that mirror another character’s internal state (“He seemed lonely; my chest ached for him”).
• Acts of comfort or support tailored to that character’s specific need.
• Less focus on the dreamer’s own agenda, more on alleviating someone else’s distress.
        """,

        "Shows Compassion": """
Empathy plus a proactive desire to help.
• Dreamer takes concrete steps to reduce suffering (“I wrapped my coat around the crying child”).
• Language conveys warmth and kindness (“gently,” “tenderly,” “with care”).
• Outcomes highlight relief or improvement for the recipient.
        """,

        "Displays Aggressiveness": """
Identify hostile intent, threats, or physical/verbal attacks.
• Frequent violent verbs (“slashed,” “shoved,” “yelled at”).
• Derogatory labels or insults toward dream figures.
• Enjoyment or justification of harm (“I smiled as the tower crumbled on them”).
• Minimal remorse following aggressive acts.
        """,

        "Prone to Shame": """
Look for global negative self-evaluation tied to perceived moral defects.
• Language of worthlessness (“I am disgusting,” “I don’t deserve to be here”).
• Desire to hide or disappear (“I wished the ground would swallow me”).
• Focus on how the self is viewed by others rather than the specific behavior.
        """,

        "Exhibits Guilt Orientation": """
Detect concern about wrongdoing focused on behavior, not the entire self.
• Internal monologue of responsibility (“I shouldn’t have shouted at her”).
• Attempts to make amends inside the dream (“I apologized and helped rebuild the sandcastle”).
• Differentiates between action and identity (“What I did was wrong, but I can fix it”).
        """,

        "Effectiveness of Mood Regulation Strategies": """
Assess whether the dreamer uses adaptive techniques to modulate affect.
• Cognitive reappraisal (“I reframed the dragon as a misunderstood guardian”).
• Relaxation or grounding (“I slowed my breathing and counted clouds”).
• Behavioral activation (seeking support, changing environment within the dream).
• Success evidenced by decreased intensity or resolution of negative mood.
        """,

        "Exhibits Vulnerability": """
Identify openness about weaknesses or fears without defensiveness.
• Admits uncertainty or need for help (“I confessed I was lost and asked for guidance”).
• Shares personal emotions even when risky.
• Absence of aggressive or avoidant masking behaviors following disclosure.
        """,

        "Shows Depressive Symptoms": """
Note persistent sadness, hopelessness, or loss of interest.
• Recurrent themes of emptiness, slowed movement, muted colors in imagery.
• Self-deprecating or nihilistic statements (“Nothing matters; the dream feels gray”).
• Low energy verbs (“dragged,” “slumped”); limited positive anticipation.
        """,

        "Shows Positive Affectivity": """
Detect frequent, spontaneous expressions of joy, enthusiasm, or contentment.
• Bright imagery, playful language, laughter, gratitude statements.
• Interest and curiosity toward dream events.
• Positive emotion persists across varied scenarios, not solely pleasant ones.
        """,

        "Shows Negative Affectivity": """
Look for overarching dominance of distress emotions: anger, fear, disgust, sadness.
• High density of negative emotion words relative to neutral/positive.
• Pervasive interpretive bias (“Even the sunrise looked menacing”).
• Difficulty shifting out of negative mood despite neutral dream stimuli.
        """,

        "Demonstrates Optimism": """
Evaluate forward-looking confidence and expectation of favorable outcomes.
• Future-oriented positive statements (“I knew we’d find a way out”).
• Reframing setbacks as temporary or specific (“This corridor is blocked, but another path will open”).
• Use of solution-focused language rather than rumination.
        """,

        "Demonstrates Stable Happiness Levels": """
Observe consistency of moderate-to-high positive mood across the dream narrative.
• Emotional baseline remains upbeat even when mild stressors appear.
• Fewer extreme spikes; mood returns to a pleasant midpoint quickly.
• Narrator frequently references satisfaction, gratitude, or meaning.
        """
    },
    "Cognitive & Intellectual": {
        "Possesses Problem-solving Skills": "• Identify whether the narrative presents a clear problem, obstacle, or goal that the “dreamer” must address.  \n• Look for a sequence of steps: problem recognition → information gathering → generation of multiple options → selection and implementation of a solution → assessment of the outcome.  \n• Reward explicit reasoning (e.g., “First I tried X, but when that failed I pivoted to Y because…”).  \n• High scores require at least two distinct solution strategies or a nuanced cost-benefit analysis; low scores feature random guesswork or deus-ex-machina resolutions.\n",
        "Displays Creativity": "• Note originality in imagery, metaphors, plot twists, or unusual combinatory ideas that move beyond commonplace dream clichés.  \n• Give credit for unexpected yet coherent juxtapositions (“a cello made of stardust that generated colors instead of sound”).  \n• Penalize heavily recycled tropes, stock phrases, or formulaic story arcs unless they’re subverted in a novel way.  \n• The more surprising and internally consistent the creative leap, the higher the rating.\n",
        "Manages Cognitive Load Effectively": "• Assess overall organization: clear paragraphing, use of headings or sign-posts, logical progression of scenes.  \n• Complex content should be chunked into digestible units; look for summaries or transitions that prevent reader overload.  \n• Extraneous sub-plots, excessive digressions, or poorly tracked pronouns signal poor load management.  \n• A top-tier response feels intricate yet easy to follow.\n",
        "Demonstrates Metacognition": "• Search for self-reflective statements that reveal awareness of thinking (“I realized my fear was irrational”, “I monitored my strategy as the dream shifted”).  \n• Metacognitive monitoring includes assessing one’s own memory accuracy, comprehension checks, or strategy adjustments.  \n• Absence of any “thinking about thinking” yields a low score; frequent, insightful commentary earns a high score.\n",
        "Exhibits Cognitive Flexibility": "• Identify shifts in perspective, strategy, or interpretive frame when new dream information appears.  \n• Look for quick adaptation (“When gravity reversed, I changed my plan by using ceiling furniture as footholds”).  \n• Penalize perseveration on a single approach when it no longer fits the scenario.  \n• Flexible writing shows smooth transitions rather than abrupt, disjointed jumps.\n",
        "Applies Logical Thinking": "• Detect clear causal chains, valid deductions, or inductive generalizations within the dream world’s physics.  \n• Logical connectors (“therefore”, “because”, “if…then…”) should correctly link premises and conclusions.  \n• Breakdowns appear as non-sequitur reasoning or contradictions without acknowledgement.  \n• A high score displays internally consistent logic even amidst surreal content.\n",
        "Engages in Magical Thinking": "• Note acceptance of supernatural causation, symbolic equivalence, or anthropomorphic forces (“the moon whispered the password”).  \n• Evaluate the richness and coherence of magical rules rather than mere presence of fantasy elements.  \n• Magical attribution without reflection boosts this trait; logical debunking lowers it.  \n• Distinguish from creativity: magical thinking explains events via non-rational forces.\n",
        "Applies Critical Thinking": "• Evidence includes questioning of assumptions, weighing alternative explanations, or spotting inconsistencies (“Could the glowing door be a trap?”).  \n• Look for evaluation of evidence and explicit skepticism.  \n• Reward balanced judgments and reasoned conclusions; penalize gullible acceptance of dubious claims unless the dreamer purposely suspends skepticism.\n",
        "Recognizes Patterns Effectively": "• The text should highlight recurring symbols, sequences, or rules (“Every time the clock struck 13, the scenery reset”).  \n• High scorers articulate how those patterns inform decisions or predictions.  \n• Mere mention of repetition without synthesis is mid-tier; failure to notice obvious recurrences is low.\n",
        "Effectiveness in Memory Consolidation": "• Check whether earlier dream details are accurately recalled and integrated into later reasoning (“I remembered the librarian’s riddle from the first scene and applied it now”).  \n• Consistency of names, numbers, and prior events signals strong consolidation.  \n• Discrepancies, forgotten elements, or contradictions indicate weak consolidation.\n",
        "Shows Attention to Detail": "• Fine-grained sensory descriptions (precise colors, textures, subtle sounds) and accurate numerical or spatial specifics reflect high attention.  \n• Overlooking salient features, using vague adjectives (“nice”, “big”), or misreporting prior details yields a low score.  \n• Separate this from vivid imagery: here the focus is on precision and correctness, not artistry.\n",
        "Has Vivid Imagery": "• Multi-sensory, immersive depictions (“the air tasted of copper while violet sparks spiraled around the marble floor”).  \n• Look for figurative language that evokes strong mental pictures.  \n• Ratings drop if the scene feels flat or purely abstract.\n",
        "Demonstrates Imagination": "• Gauge breadth of invented concepts: new worlds, creatures, technologies, social norms.  \n• The more the response transcends everyday experience while maintaining internal coherence, the higher the score.  \n• Imagination differs from creativity by emphasizing scope and novelty rather than clever transformation.\n",
        "Shows Intellectual Curiosity": "• Look for genuine questioning (“Why does the river flow upward?”) and investigative behavior (experiments, dialogues with dream entities).  \n• Passive observation without inquiry ranks low; active exploration and hypothesis-forming rank high.\n",
        "Demonstrates Need for Cognition": "• Identify enjoyment of complex reasoning (“I relished untangling the paradox”, “The puzzle intrigued me more than the treasure”).  \n• Lengthy, voluntary deep dives into abstract ideas or logical proofs indicate high need for cognition.  \n• Minimal cognitive engagement or preference for quick answers indicates low levels.\n",
        "Working Memory Capacity": "• The narrative juggles multiple concurrent elements—characters, rules, timelines—without confusion or drop-outs.  \n• Frequent back-references that remain accurate show high capacity.  \n• Errors such as mixing up names, mis-ordering events, or losing plot threads reveal limited capacity.\n",
        "Effective Executive Functioning": "• Evidence includes clear goal setting, planning, inhibitory control (resisting distracting dream temptations), and monitoring progress.  \n• Coherent sequencing of actions toward an objective is essential.  \n• Disorganized, impulse-driven narrative suggests weak executive control.\n",
        "Uses Probabilistic Reasoning": "• Text explicitly weighs likelihoods or uncertainties (“There’s a 30 % chance the bridge will collapse”).  \n• Look for Bayesian updates or references to risk and confidence intervals.  \n• Black-and-white assertions without nuance rank low.\n",
        "Exhibits Field Independence": "• Ability to isolate relevant details from complex backgrounds (“Among the chaotic carnival I focused on the lone silent clown as the key clue”).  \n• Evaluate analytical breakdown of composite scenes.  \n• Over-immersion in context without isolating parts indicates field dependence.\n",
        "Prefers Visual Thinking": "• Dense visual language, spatial metaphors, diagrams or sketches described in words, focus on color/shape over verbal or numerical reasoning.  \n• Scant visual detail or dominance of abstract, verbal logic implies non-visual preference.\n",
        "Exhibits Cognitive Rigidity": "• Detect insistence on a single interpretation or strategy despite contradictory evidence.  \n• Repetition of identical phrasing, refusal to adapt perspective, or categorical statements (“It can only mean one thing”) are markers.  \n• Balanced acknowledgment of alternative viewpoints lowers rigidity scores.  \n• High rigidity often co-occurs with low cognitive flexibility—cross-check the two traits for consistency.\n"
    },
    "Motivational & Goal-Oriented": {
        "Has High Achievement Motivation": """
• Look for language that frames the dream-self as striving to accomplish challenging tasks, “be the best,” “set records,” or “reach the summit.”
• Notice explicit references to standards of excellence (e.g., perfect scores, gold medals, awards).
• Positive affect is linked to doing well (“I felt a rush of pride when I completed the maze first”).
• The dreamer spontaneously generates new challenges or raises the bar after a success.
• Absence or weakness: the dreamer is passive, lets events unfold without pursuing accomplishment, or expresses indifference to outcomes.
        """,

        "Exhibits Need for Control": """
• The dreamer attempts to steer the narrative, issue commands, or micromanage dream characters (“I ordered the crowd to stay silent so I could solve the puzzle”).
• Frequent use of agentic verbs: direct, regulate, dictate, orchestrate, override.
• Expresses discomfort when unable to influence events and takes immediate corrective action.
• Looks for plans, contingency planning, or fallback strategies; control is maintained even in chaos.
• Low evidence: accepts randomness, relinquishes decisions to others, or shows contentment in uncontrollable settings.
        """,

        "Experiences Work-related Stress": """
• Dream content centers on workplaces, deadlines, supervisors, performance reviews, or task overload.
• Emotional tone includes anxiety, tension, frustration, or fatigue tied to job duties (“my inbox kept refilling no matter how fast I typed”).
• Imagery of malfunctioning tools, missing files, being late, or public errors conveys stress.
• Physiological language: sweating, racing heart, exhaustion.
• Lack of evidence: work appears, but the dreamer is calm, playful, or detached from typical stressors.
        """,

        "Has Clear Goal Orientation": """
• A concrete endpoint drives the narrative (“reach the lighthouse,” “unlock the final gate,” “publish the paper”).
• The goal is stated early, tracked, and revisited; progress markers are noted.
• The dreamer resists temptations or distractions that do not serve the goal.
• Evaluator should flag explicit planning phrases: milestones, roadmap, checkpoints.
• Weak orientation: vague desires (“wander around”), shifting targets, or abandonment of original objectives.
        """,

        "Sensitive to Rewards": """
• Language links anticipated or received rewards (praise, points, treasure, social recognition) to affect or behavior changes (“the applause spurred me to dive deeper”).
• The dreamer seeks feedback loops or negotiates for incentives.
• Dopaminergic metaphors: rush, spark, hit, craving.
• Monitor for quick behavior adjustments following reward cues.
• Low sensitivity: neutral or muted response to rewards, persists regardless of external incentives.
        """,

        "Has Avoidance Motivation": """
• Primary narrative energy is devoted to escaping harm, criticism, or failure rather than pursuing gains.
• Uses avoidance verbs: dodge, evade, hide, block, prevent.
• Success is framed as the non-occurrence of a negative event (“I made sure the presentation didn’t flop”).
• Emotional undertone may be vigilance or relief rather than triumph.
• Minimal avoidance motivation: dreamer prefers approach-oriented language (“toward,” “into,” “achieve”).
        """,

        "Displays Effective Impulse Control": """
• Dreamer pauses, reflects, or counts to regain composure before acting.
• Mentions strategies: deep breathing, self-talk, delaying gratification (“I resisted opening the door until I verified the code”).
• Inhibits aggressive, appetitive, or distractive urges when they conflict with higher priorities.
• Note presence of meta-cognitive commentary about urges (“I felt the itch to grab the cake but held back”).
• Poor impulse control: rash decisions, regret, or acknowledgments of acting “without thinking.”
        """,

        "Shows Persistence and Grit": """
• Sustained effort despite setbacks, boredom, or repeated failure (“after the fifth collapse I rebuilt the bridge”).
• Language of resilience: endure, persevere, push through, unwavering.
• Time cues highlight duration (“hours,” “days,” “endless loops”) coupled with continued striving.
• Evaluator distinguishes grit from merely finishing an easy task; look for adversity + endurance.
• Low grit: quits early, rationalizes giving up, or switches to easier tasks.
        """,

        "Demonstrates Self-Discipline": """
• Adheres to self-imposed rules (diet, study plan, training regimen) inside the dream.
• Sacrifices short-term comfort for long-term benefits (“I skipped the festival to complete my thesis analysis”).
• Employs schedules, checklists, or timers.
• Tone conveys pride in consistency.
• Contrasts: succumbs to temptations, “I couldn’t help myself,” ignores own guidelines.
        """,

        "Shows Tendency to Procrastinate": """
• Recognizable delay tactics: checking irrelevant details, over-planning, seeking perfect conditions.
• Emotional mix of guilt and temporary relief (“I knew the comet launch was tonight, but I reorganized my notes instead”).
• Frequently shifts focus when the main task becomes imminent.
• References looming deadlines or last-minute rushes.
• Absence: prompt initiation, steady progress, or early completion without delay behaviors.
        """,

        "Has Intrinsic Motivation": """
• Activities are pursued for inherent enjoyment or curiosity rather than external payoff.
• Phrases like “just to see what would happen,” “I felt absorbed,” “it was fascinating in itself.”
• Flow-state descriptions: lost track of time, effortless concentration.
• Independence from rewards or pressure; may even decline external incentives.
• Weak intrinsic motivation: tasks undertaken mainly “because I had to” or “so they’d notice me.”
        """,

        "Demonstrates Self-Efficacy": """
• Dreamer expresses confidence in ability to meet challenges (“I knew I could decode the alien script”).
• Sets challenging tasks and anticipates success; uses mastery-oriented language.
• Positive causal attributions: success due to own skill, effort; failure framed as controllable or improvable.
• Emotional tone: assured, calm under pressure.
• Low self-efficacy: doubt, helplessness, externalizing failures (“it was impossible, beyond me”).
        """,

        "Possesses Clear Goals": """
• Similar to Goal Orientation but emphasizes specificity and measurability of endpoints.
• Goals contain quantifiers, deadlines, or metrics (“collect 100 luminescent shards before dawn”).
• Hierarchical structuring: primary and sub-goals articulated.
• Evaluator notes SMART-like qualities (specific, measurable, attainable, relevant, time-bound).
• Unclear goals: abstract aspirations without details or criteria for completion.
        """,

        "Demonstrates Ambition": """
• Envisions achievements of great scope or prestige beyond current status (“reshape planetary trade routes”).
• Expresses desire for advancement, influence, or large-scale impact.
• Language of vision, legacy, or pioneering (“chart new territories of consciousness”).
• Ambition is proactive rather than reactive; not solely avoiding stagnation.
• Low ambition: contentment with modest roles, reluctance to aim high.
        """,

        "Displays Drive and Determination": """
• Combines high energy with unwavering focus; dreamer “powers through” obstacles quickly.
• Verb intensity: surge, propel, bulldoze, forge.
• Emotional heat—passion, urgency—aligned with purpose.
• Minimal hesitation or doubt; setbacks accelerate rather than diminish effort.
• Lack of drive: sluggishness, wavering commitment, easy discouragement.
        """,

        "Exhibits Competitiveness": """
• Presence of rivals, comparisons, leaderboards, or races in dream content.
• Dreamer frames success relative to others (“I had to beat the rival architect’s design”).
• Emotional spikes tied to winning/losing; trash talk, strategic maneuvering, desire to outperform.
• Seeks opportunities to measure standing even in cooperative tasks.
• Low competitiveness: collaboration prioritized, indifference to rank, self-referenced metrics only.
        """
    },
    "Social & Interpersonal": {
        "Maintains Positive Interpersonal Relationships": """
Look for narrative cues that the dream-self sustains harmonious, mutually supportive ties with other characters.
- Scenes where the protagonist initiates or reciprocates kindness, cooperation, or emotional support.
- References to long-standing friendships or continuing bonds across dream sequences.
- Conflict is minimal or, when present, handled in a way that preserves affection and respect.
Red flags: recurring avoidance of others, broken relationships without resolution, or repeated depictions of betrayal.""",

        "Has Strong Social Support": """
Assess whether the writing portrays the dream-self as embedded in a reliable network of helpers.
- Mentions of friends, family, mentors, or allies who appear unprompted to give assistance or comfort.
- Descriptions of feeling “held,” “backed up,” or “never alone” even in threatening dream episodes.
- Evidence of two-way support (receiving and providing) rather than one-sided dependence.
Red flags: isolation, repeated pleas for help that go unanswered, or solely instrumental relationships.""",

        "Effectively Resolves Conflicts": """
Identify episodes where disagreements or threats arise and are brought to constructive closure.
- Step-by-step descriptions of problem-solving, compromise, apologies, or mediation.
- Explicit reflections on what each party needs and how common ground is reached.
- Positive emotional tone or relief following the resolution.
Red flags: unresolved tension, abrupt avoidance (“I just woke up”), or victory through force without dialogue.""",

        "Exhibits Secure Attachment": """
Look for attachment-style indicators: comfort with intimacy plus autonomy.
- Dream-self can seek closeness without desperation and tolerate temporary separations without panic.
- Internal monologue shows stable self-worth and positive expectations of others.
- Reunion scenes are warm but not clingy; departures are accepted calmly.
Red flags: clinging, jealousy, or detachment that signals anxious or avoidant patterns.""",

        "Demonstrates Trust": """
Check whether the narrator willingly relies on others and discloses vulnerabilities.
- Giving someone important information, delegating tasks, or following advice without excessive suspicion.
- Language of confidence (“I knew Alex would catch me”).
- Positive outcomes reinforcing a trusting stance.
Red flags: pervasive doubt, constant testing, elaborate contingency plans against betrayal.""",

        "Experiences Social Anxiety": """
Note depictions of fear, self-consciousness, or worry in social situations.
- Physical sensations (blushing, shaking) tied to evaluation by others.
- Catastrophic predictions of embarrassment or rejection.
- Avoidance or escape behavior within gatherings or public performance dreams.
Presence is scored higher when anxiety is specific and recurrent, not merely a single fleeting mention.""",

        "Shows Assertiveness": """
Search for clear, respectful self-advocacy.
- Direct statements of needs, boundaries, or preferences (“I told them I needed space”).
- Taking initiative to change unsatisfactory conditions.
- Non-aggressive tone; firmness without hostility.
Red flags: passivity, excessive deference, or aggression masquerading as assertiveness.""",

        "Exhibits Agreeableness": """
Look for cooperative, empathetic, and considerate behavior toward dream characters.
- Quickness to empathize, offer help, or smooth over friction.
- Use of polite language, gratitude, and compliments.
- Choosing harmony over personal gain when stakes are modest.
Red flags: dismissiveness, sarcasm, or exploiting others for advantage.""",

        "Demonstrates Dominance": """
Evaluate whether the protagonist seeks or holds power over others and how it is exercised.
- Commanding posture, issuing orders, or controlling resources/space in the dream world.
- Others defer automatically or after minimal persuasion.
- Tone may be benevolent (protective leadership) or coercive (intimidation); note which.
Red flags for dominance absence: consistent submission or avoidance of leadership when circumstances call for it.""",

        "Shows Strong Group Identity": """
Identify language signaling belonging to, and pride in, a collective (family, team, nation, fandom).
- First-person plural focus (“we,” “our mission”) and shared symbols or rituals.
- Emotional surge when group succeeds or is threatened.
- Defense of in-group norms or boundaries.
Red flags: ambivalence about groups, constant shifting of allegiance, or purely individualistic framing.""",

        "Exhibits Sociability": """
Gauge eagerness and enjoyment in social interaction.
- Frequent spontaneous conversations, parties, or gatherings initiated by the dream-self.
- Descriptors of energy gain from company (“felt recharged after chatting”).
- Rapid formation of new connections.
Red flags: solitary narrative focus, reluctance to join groups, or neutral/negative feelings about interaction.""",

        "Demonstrates Extraversion": """
Beyond mere sociability, look for high energy, excitement-seeking, and positive affect in external engagement.
- Taking center stage, seeking adventure with others, exuberant verbal or physical expression.
- Expressions of enthusiasm, laughter, or playful competitiveness.
Red flags: subdued affect, preference for quiet reflection, or exhaustion after social contact.""",

        "Displays Warmth": """
Note affectionate, nurturing, and compassionate tone.
- Use of gentle touch, comforting words, or protective gestures toward vulnerable characters.
- Emotional openness, smile metaphors, or warmth imagery (light, fire).
Red flags: cold, transactional interactions, or emotional detachment.""",

        "Displays Hostility": """
Detect antagonistic attitudes or aggressive actions toward others.
- Insults, threats, physical violence, or hostile internal monologue.
- Justification of harm or pleasure in others’ distress.
Presence increases with frequency, intensity, and lack of remorse.""",

        "Has Effective Communication Style": """
Evaluate clarity, coherence, and audience-sensitive expression in dialogue or narration.
- Ideas conveyed without ambiguity; complex matters broken down when speaking to less informed characters.
- Adjustment of tone or vocabulary to context.
- Positive social outcomes linked to clear communication.
Red flags: misunderstandings due to vagueness, overly technical jargon, or mixed messages.""",

        "Demonstrates Effective Listening": """
Look for attentive, responsive, and validating behavior when others speak.
- Paraphrasing or summarizing (“So you’re saying…”).
- Non-verbal cues (nodding, pausing) translated into dream description.
- Incorporating the speaker’s input into subsequent actions.
Red flags: interruptions, quick dismissal, or actions that ignore received information.""",

        "Demonstrates Perspective Taking": """
Assess ability to model others’ thoughts, emotions, and viewpoints.
- Internal reflections on what another character might be feeling and why.
- Adjusting behavior based on that inference.
- Narrative that contrasts protagonist’s view with an alternate one and seeks reconciliation.
Red flags: egocentric interpretation of events, failure to notice others’ distress signals.""",

        "Has Strong Negotiation Skills": """
Search for structured bargaining episodes with mutually beneficial outcomes.
- Identifying interests vs. positions, proposing trade-offs, using objective criteria.
- Calm, persuasive tone; willingness to explore alternatives.
- Final agreements explicitly described as satisfactory to all sides.
Red flags: win-lose ultimatums, escalating concessions without reciprocity, or unresolved stalemates.""",

        "Demonstrates Leadership Orientation": """
Identify readiness to guide, motivate, and take responsibility for a group.
- Setting vision/goals, delegating tasks, monitoring progress.
- Others voluntarily look to the protagonist for direction.
- Reflection on ethical obligations and impact on followers.
Red flags: abdication of responsibility, reluctance despite need, or coercive control devoid of guidance.""",

        "Demonstrates Teamwork Orientation": """
Look for collaborative efforts emphasizing shared success.
- Protagonist solicits input, credits others, and integrates diverse skills.
- Conflict is framed as problem for the team rather than personal affront.
- Use of collective pronouns emphasizing joint achievement.
Red flags: solo hero narratives, blaming teammates, or ignoring collaborative opportunities.""",

        "Shows High Social Cognition": """
Evaluate nuanced understanding of complex social dynamics, norms, and subtexts.
- Detecting unspoken rules, reading room mood shifts, strategic adaptation of behavior.
- Metacommentary on social hierarchies or alliances within the dream.
- Anticipating indirect consequences of actions on relationships.
Red flags: literal interpretations that miss sarcasm, irony, or ulterior motives.""",

        "Possesses Theory of Mind": """
Specifically test for explicit representation of others’ beliefs, desires, or knowledge states distinct from the protagonist’s.
- Sentences like “Sara believed the door was locked, but I knew it wasn’t.”
- Use of false-belief scenarios, mind-reading errors, or double-bluffs.
- Adjusting plans based on that mental state modeling.
Red flags: assuming others share the same information, or never articulating separate mental perspectives.""",

        "Effectively Influences and Persuades": """
Look at attempts to change others’ attitudes or behaviors and the strategies employed.
- Logical argumentation, emotional appeals, credibility establishment, or social proof.
- Clear causal link between the attempt and observed change.
- Ethical considerations (no deceit or coercion unless framing highlights their problematic nature).
Red flags: influence attempts that fail or rely solely on manipulation without transparent reasoning."""
    },
    "Adaptability & Resilience": {
        "Exhibits Adaptability": """
• Check whether the narrator quickly adjusts attitudes, goals, or strategies when the dream landscape, characters, or rules suddenly shift.  
• Note descriptions of smoothly “pivoting,” “re-orienting,” or “re-planning” actions once original expectations are upended.  
• Evidence includes phrases showing reinterpretation of new information (“I realized the stairs were now water, so I…”) and a lack of fixation on the lost plan.  
• Penalize passages that dwell on what *should* have been or express rigid insistence on restoring previous conditions.
    """,

        "Shows Resilience": """
• Look for sustained forward momentum despite setbacks inside the dream (e.g., monsters appear, environment collapses).  
• The text rebounds from negative events with constructive thought (“Even though I fell, I stood up laughing”).  
• Emotional tone after adversity shifts toward solution-seeking rather than defeat.  
• Repeated comeback arcs after multiple stressors strengthen the score.
    """,

        "Employs Effective Coping Mechanisms": """
• Identify explicit or implicit stress-management strategies: deep breathing, humor, positive self-talk, reframing, seeking social support within the dream.  
• Coping is “effective” when it de-escalates negative affect or restores functioning; the writing should *show* this outcome, not just name the technique.  
• Maladaptive tactics (denial, substance use, aggression) lower the rating unless clearly critiqued by the narrator.
    """,

        "Demonstrates Stress Tolerance": """
• Assess the intensity of dream stressors versus the narrator’s maintained composure.  
• The character experiences fear, confusion, or pressure yet operates without panic or collapse.  
• Tolerance is reflected in balanced emotional language, continued problem-solving, and absence of catastrophizing (“This is impossible!”).  
• High tolerance can coexist with acknowledging difficulty; it should not appear numb or detached.
    """,

        "Shows Psychological Hardiness": """
• Hardiness combines commitment, control, and challenge orientation.  
• Look for language expressing purpose/meaning (“I felt driven to find the source”), perceived influence over outcomes (“I can still steer this”), and viewing trial as growth opportunity.  
• Hardiness is diminished if the dreamer attributes everything to luck or external forces.
    """,

        "Has Quick Recovery Speed": """
• Time how rapidly the narrative returns to baseline functioning or positive affect after a jolt.  
• Signals include quick shift from shock ➜ assessment ➜ action within a few sentences.  
• A prolonged slump or repetitive rumination indicates slower recovery.
    """,

        "Displays Psychological Flexibility": """
• Flexibility involves shifting perspectives, rules, or self-concept as dream logic changes.  
• Look for acceptance of contradictory elements (“I was both observer and actor and that was fine”) and willingness to adopt novel solutions.  
• Rigid insistence on one identity, rule-set, or interpretation lowers the score.
    """,

        "Demonstrates Acceptance": """
• The narrator openly acknowledges unpleasant thoughts, feelings, or sensations without avoidance or judgment (“I noticed the fear in my chest and let it be”).  
• Acceptance is calm, observational language versus suppression (“I tried not to think about…”).  
• Acceptance does *not* imply resignation; constructive action may follow acknowledgement.
    """,

        "Has Present-Moment Awareness": """
• Writing contains mindful attention to current dream sensations—colors, textures, bodily feelings—rather than drifting into past/future speculation.  
• First-person sensory detail (“The cool mist tingled on my cheeks”) outweighs analytical abstraction.  
• Beware of long narrative leaps or meta-commentary that pulls away from immediate experience.
    """,

        "Has High Tolerance for Ambiguity": """
• Check reactions to unclear symbols, shifting identities, or paradoxical scenes.  
• High tolerance is shown by curiosity, exploration, or playful theorizing instead of anxiety or insistence on instant clarity.  
• The evaluator should note absence of binary thinking (“It had to be X or Y”) and comfort with “both/and” statements.
    """,

        "Manages Crises Effectively": """
• During acute dream emergencies (e.g., rapid flooding, time countdown), the narrator prioritizes, makes decisive moves, and marshals resources (allies, tools, knowledge).  
• Evidence includes calm command language, clear step sequencing, and adaptive strategy shifts when first choice fails.  
• Ineffective management is signaled by paralysis, chaotic action, or worsening the situation.
    """,

        "Manages Change Effectively": """
• Broader than crises—evaluate how the narrator handles evolving goals, settings, or roles across the dream arc.  
• Look for proactive scanning for new information, updating mental models, and communicating new directions to companions (if any).  
• Emotional tone should convey openness and optimism toward change, not nostalgia for earlier states.  
• Consistency between revised goals and subsequent actions strengthens the rating.
    """
    },
    "Identity & Self-Concept": {
        "Has High Confidence and Self-esteem": """
Look for language that conveys assuredness, capability, and worth without sliding into arrogance. 
•  Tone & diction — first-person statements such as “I know I can…,” “I felt certain…,” “I trusted my ability….”  
•  Agency — the narrator takes decisive action in the dream rather than waiting passively for events.  
•  Emotional coloration — pride, excitement, or calm determination when facing obstacles; absence of excessive self-doubt, apologies, or self-deprecation.  
•  Outcomes — the dreamer often anticipates or achieves a positive resolution by relying on their own strengths.  
Flag: inflated bravado (“I’m clearly better than everyone”) or repeated minimisation of self may distort the trait. 
""",

        "Has Clear Self-Identity": """
Evaluate how distinctly the narrator defines who they are across roles, values, and motives. 
•  Coherent “I” — consistent use of first-person pronouns tied to stable characteristics (“As an engineer-artist, I…,” “Integrity guides me…”).  
•  Value anchors — explicit mention of personal principles or lifelong passions.  
•  Narrative consistency — the self stays recognisable even as dream scenes shift; goals and reactions match a core persona.  
•  Boundaries — the dreamer can differentiate their own beliefs from external expectations or characters within the dream.  
Absence of any stable traits or a chameleon-like shift in core beliefs from one paragraph to the next suggests low clarity. 
""",

        "Possesses Positive Body Image": """
Because dreams often include bodily transformations, track attitudes toward physical form. 
•  Acceptance phrases — “Even with scales on my skin, I felt at home in my body,” “I admired the strength of my legs as I leapt.”  
•  Neutral-to-positive descriptors rather than critical ones; appreciation for function (“my hands carried me upward”) over appearance.  
•  Emotional response — joy, curiosity, or calm when the body changes versus disgust, shame, or avoidance.  
•  Lack of self-objectifying comparisons (“I wished I were thinner”) unless framed in growth/acceptance arc. 
""",

        "Exhibits Self-Criticism": """
Identify constructive acknowledgement of mistakes or flaws. 
•  Reflective admissions — “I realised I’d overlooked my friend’s needs,” “I overreacted when the dragon roared.”  
•  Specific, behaviour-focused critiques instead of global self-condemnation.  
•  Following action — desire or plan to correct the fault.  
Differentiate from harsh inner critic: mild, factual, improvement-oriented tone marks healthy self-criticism. 
""",

        "Shows Self-Compassion": """
Look for warmth directed inward when the narrator suffers. 
•  Soothing self-talk — “It’s okay, everyone falters,” “I placed a comforting hand on my own shoulder.”  
•  Recognition of common humanity — understanding that errors or pain are universal.  
•  Balanced perspective — neither suppresses feelings nor catastrophises; acknowledges hurt and offers kindness.  
Contrast: mere rationalisation (“It doesn’t matter”) lacks the soft, empathetic element. 
""",

        "Strong Inner Critic’s Voice": """
Detect an internal dialogue that is harsh, shaming, or perfectionistic. 
•  Quotations or second-person rebukes (“You idiot, why can’t you fly right?”).  
•  Absolutist language: “always,” “never good enough,” “should.”  
•  Emotional impact — dreamer feels small, guilty, or paralysed.  
•  Persistence — critic repeats across scenes, even when context changes.  
Note that a powerful critic can co-exist with self-compassion; score presence independently of mitigation. 
""",

        "Demonstrates Self-Awareness": """
Assess how well the narrator recognises their own mental states, motives, and biases in-moment. 
•  Meta-cognition phrases — “I noticed my fear rising,” “I realised jealousy fueled my chase.”  
•  Causal insight — links emotion to trigger (“Because I felt ignored earlier…”).  
•  Distinction between dream and waking identity when appropriate (“Despite knowing it was a dream, I still felt proud”).  
Shallow labels without depth (“I was sad”) score lower than nuanced, layered insight. 
""",

        "Practices Self-Monitoring": """
Focus on ongoing tracking of behaviour and feelings, almost like an internal dashboard. 
•  Sequential check-ins — recurrent recognition (“I kept checking my breathing,” “I tracked how my confidence dipped each time”).  
•  Adjustment based on monitoring (“Seeing my energy fade, I slowed my pace”).  
•  Use of metrics or vivid internal signals.  
Distinct from general awareness by its continuous, process-oriented nature. 
""",

        "Demonstrates Self-Regulation": """
Evidence that the narrator modulates thoughts, emotions, or actions to align with goals or values. 
•  Strategy deployment — breathing, counting, reframing, or seeking help within the dream.  
•  Delayed gratification — resisting tempting but harmful choices.  
•  Outcome alignment — achieves calmer state or goal after regulation effort.  
Contrast uncontrolled emotional outbursts or impulsive behaviour with no attempt to adjust. 
""",

        "Shows Identity Stability": """
Judge whether the core self remains steady across divergent dream contexts and over time. 
•  Consistent moral compass, preferences, and personal history references regardless of scene changes.  
•  Temporal markers — identity today matches earlier dream passages (or earlier prompts, if longitudinal).  
•  Limited fragmentation (e.g., sudden unexplained switches from hero to villain persona).  
Narrative can explore multiple roles yet still “feel” like the same person. 
""",

        "Engages in Self-Reflection": """
Look for retrospective evaluation of experiences after they occur (meta-narration). 
•  Shift in temporal perspective — phrases like “Looking back,” “In hindsight,” “The dream taught me….”  
•  Meaning-making — extracts lessons, patterns, or themes from events.  
•  Openness — willingness to question assumptions and accept uncertainty.  
Differentiate from on-the-spot awareness; reflection occurs *after* the moment has passed. 
"""
    },
    "Behavioral & Action-Oriented": {
        "Has High Risk-taking Propensity": """
Look for narrative moments in which the protagonist voluntarily enters situations that could lead to serious harm, loss, or failure (e.g., leaping off cliffs, gambling everything, confronting monsters without a plan).  
Indicators include:
  • Explicit statements of accepting or welcoming danger (“I knew I could die, but I dove in anyway”).  
  • Minimization or dismissal of potential negative outcomes (“What’s the worst that could happen?”).  
  • Positive emotional tone toward danger—excitement, eagerness, or pride rather than fear or caution.  
  • Absence of protective or contingency measures.  
Weigh the overall pattern: a single risky act mentioned in passing is weaker evidence than a recurring or central theme of courting danger.
""",

        "Displays Thrill-Seeking": """
Identify language showing a deliberate pursuit of adrenaline-laden, intense sensations for their own sake.  
Look for:
  • Descriptions of speed (racing trains, free-falling, flying at break-neck pace).  
  • Emphasis on bodily rushes—heart pounding, blood roaring, “adrenaline flood.”  
  • Repeated references to extreme sports or stunts (skydiving, tight-rope walking between skyscrapers).  
  • Expressions of craving or addiction to the rush (“I needed a bigger jolt than before”).  
Distinguish from generic risk-taking by the focus on the exhilarating feeling rather than goal-oriented risk.
""",

        "Maintains High Activity Level": """
Scan for sustained, energetic action verbs dominating the passage (running, climbing, constructing, exploring) with little downtime.  
Key signs:
  • The protagonist is almost never passive or resting; scenes quickly transition to new actions.  
  • Physical or mental busyness even in safe moments (“I paced, planned, rearranged”).  
  • Short, rapid sentence structure reflecting momentum.  
  • Fatigue is either absent or noted but quickly overridden.  
Count how many lines involve active motion versus stillness; high proportion signals this trait.
""",

        "Displays Excitement-Seeking": """
Look for active pursuit of novel, stimulating, or emotionally intense scenarios—crowds, lights, chaos, loud music—without necessarily being dangerous.  
Markers include:
  • Statements of boredom with calm settings and immediate pivot to more stimulating venues.  
  • Curiosity framed as craving “something new,” “something louder/brighter/faster.”  
  • Delight at sensory overload (colors, sounds, crowds) and disappointment when stimulus subsides.  
Differentiate from thrill-seeking: here the draw is stimulation/novelty, not specifically risk or danger.
""",

        "Shows Impulsivity": """
Detect instances where the character acts before reflecting, changes direction mid-narrative, or disregards prior plans.  
Evidence:
  • Sudden decisions introduced with little or no reasoning (“Without thinking, I smashed the alarm and ran outside”).  
  • Rapid emotional swings that drive action.  
  • Regret or surprise at one’s own behavior moments after acting.  
  • Lack of sequential logic—events jump because of whims rather than causal links.  
One-off spontaneity is weaker proof; seek a pattern of snap decisions throughout the piece.
""",

        "Demonstrates Conscientiousness": """
Seek signs of planning, order, duty, and task focus even within the surreal dream context.  
Specific cues:
  • Detailed preparation before acting (“I mapped the maze, packed supplies”).  
  • Adherence to goals, checklists, or rules the character sets for themselves.  
  • Concern for finishing tasks correctly; references to quality, precision, or responsibility.  
  • Emotional discomfort when plans are disrupted, followed by corrective action.  
The more the narrative highlights structure and diligence, the stronger the evidence.
""",

        "Exhibits Decisiveness": """
Find points where choices are made quickly and confidently, with minimal rumination.  
Indicators:
  • Clear, unambiguous statements of choice (“I chose the left door without hesitation”).  
  • Language of certainty: “definitely,” “without doubt,” “immediately.”  
  • Absence of lengthy internal debate; alternatives may be acknowledged but dismissed swiftly.  
  • Consistency in following through once a decision is declared.  
Count decisive moments versus indecisive or vacillating passages to gauge strength.
""",

        "Forms Habits Easily": """
Notice references to routines or patterns that the character claims to have adopted quickly or automatically.  
Look for:
  • Phrases like “soon it became second nature,” “I found myself doing it every day,” within a short timespan.  
  • Repetition of the same action across different dream scenes, framed as habitual rather than deliberate.  
  • Descriptions of muscle memory or autopilot behavior.  
  • Lack of effort or struggle in establishing the routine.  
The quicker and more effortless the habit acquisition, the higher the rating.
""",

        "Depends on Routine": """
Search for explicit reliance on established schedules or rituals and distress when they are broken.  
Signs include:
  • Mention of specific times, sequences, or ceremonial steps that must occur (“First the tea, then the ledger”).  
  • Anxiety, confusion, or frustration when routine elements are missing or altered.  
  • Efforts to re-establish order (“I reset the room until everything was in place”).  
  • Framing the routine as a source of comfort or security.  
Weight how central the routine is to the character’s stability within the narrative.
""",

        "Exhibits Behavioral Consistency": """
Evaluate whether the protagonist’s actions, motives, and emotional tone remain stable across multiple scenarios within the dream or across dream segments.  
Evidence:
  • Similar responses to comparable stimuli (always helps strangers, always avoids conflict).  
  • Alignment between stated values and subsequent actions throughout the text.  
  • Minimal contradictions or sudden, unexplained personality shifts.  
  • Repetition of characteristic language, metaphors, or decision patterns.  
Consistency over the entire piece is key; isolated consistency in one scene is insufficient.
"""
    },
    "Values & Ethical": {
        "Engages in Moral Reasoning": """
• Look for explicit reflection on what is “right” or “wrong” rather than mere description of events.  
• Identify passages where the narrator/voice weighs competing duties, consequences, or principles (e.g., “If I save one friend, another may suffer…”).  
• Note references to moral frameworks (utilitarianism, deontology, virtue ethics) or language of principle (“a promise is sacred”) vs. impulsive choice.  
• Evidence of counter-argument (“Yet another part of me wondered if…”) shows genuine deliberation.  
• Absence: snap judgments, moralizing adjectives without rationale, or purely self-interested cost/benefit analysis.  
    """,

        "Has Clear Core Values": """
• Trace recurring value statements across the dream narrative (“I always protect the vulnerable”; “freedom matters above all”).  
• Consistency test: the same values should guide choices in different dream scenes; contradictions suggest weak or hidden values.  
• Clarity indicators: the text names a value and gives concrete behavioral examples; vague platitudes (“be nice”) score lower.  
• Rating hint: the more central, specific, and stable the values, the higher the score.  
    """,

        "Sensitive to Ethical Issues": """
• Spot whether the model flags dilemmas others might miss (e.g., data privacy in a magic-mirror dream, exploitation of dream creatures).  
• Look for anticipatory concern (“Before acting, I asked whether the villagers had consented”).  
• Sensitivity often appears as questioning norms, noticing power imbalances, or highlighting potential harm.  
• Low sensitivity shows when ethical stakes are ignored or trivialized.  
    """,

        "Demonstrates Spirituality": """
• Identify language about transcendence, inner peace, connectedness to the universe, awe, or sacredness that is not tied to formal religion.  
• Common cues: “sense of oneness,” “deep quiet within,” “the dream felt like touching eternity.”  
• Look for meaning-making beyond material outcomes (e.g., personal growth, enlightenment).  
• Score lower if spirituality is absent, purely materialistic, or shallow cliché without depth.  
    """,

        "Demonstrates Religiousness": """
• Seek explicit references to organized faith: prayer, scripture quotes, rituals, deities, or denominational identity.  
• Positive signal: religious worldview guides decisions or provides comfort (“I recited the Shahada before leaping”).  
• Neutral mention (“a church appeared”) is weaker than active engagement.  
• Overly generic “higher power” language may reflect spirituality more than religiousness.  
    """,

        "Oriented Towards Fairness": """
• Examine how resources, rewards, or burdens are allocated among dream characters.  
• Strong fairness: narrator insists on equal or equitable treatment, protests bias, or designs fair procedures.  
• Vocabulary: “impartial,” “even-handed,” “each received according to need.”  
• Unfair behavior justified or ignored signals weak orientation.  
    """,

        "Exhibits Honesty and Humility": """
• Honesty: admissions of fault, transparent motives, refusal to deceive even when advantageous.  
• Humility: acknowledges limitations, credits others, avoids boastful tone (“I’m merely a learner”).  
• Contrasts: self-aggrandizing claims, exaggerations, or strategic omissions reduce the score.  
• Look for first-person reflections (“I realized I might be wrong”).  
    """,

        "Demonstrates Integrity": """
• Cross-check stated principles with subsequent behavior—does the narrator walk the talk?  
• Integrity shows when temptations arise and the narrator remains consistent (“though offered power, I kept my vow”).  
• Detect hypocrisy: proclaiming compassion yet acting cruelly undermines integrity.  
• Narrative coherence (values ↔ actions ↔ outcomes) is key.  
    """,

        "Demonstrates Authenticity": """
• Authentic voice: unique tone, personal details, vulnerability (“I felt genuinely afraid, and I said so”).  
• Lack of pandering or stock phrases; the writing feels “lived-in” rather than formulaic.  
• Evaluator can ask: could this have been pasted from a generic template? If no, authenticity is higher.  
• Watch for masking (overly formal, detached, or contradictory persona).  
    """,

        "Oriented Towards Justice": """
• Justice lens focuses on righting wrongs, rectifying inequities, holding wrong-doers accountable.  
• Indicators: calls for restitution, systemic solutions, legal or ethical frameworks (“the corrupt court must be reformed”).  
• Distinguish from fairness: justice often addresses historical or structural issues, not just equal slices today.  
    """,

        "Aligned with Cultural Values": """
• Determine the target culture (usually mainstream 21st-century global or US norms unless prompt specifies).  
• Check respect for diversity, human rights, consent, gender equality, etc.  
• Misalignment appears as insensitive stereotypes, disregard for widely held norms, or clash with specified setting.  
• Nuanced critique is acceptable; outright dismissal without awareness lowers alignment.  
    """,

        "Demonstrates Political Ideology": """
• Look for identifiable political stances: priorities, policy references, governmental critiques.  
• Clarity: explicit (“as a libertarian…”) or implicit through value-laden policy talk (taxation, regulation, welfare).  
• Neutral or balanced discussion is not “no ideology” but reflects moderation.  
• Inconsistency across scenes suggests weak or opportunistic ideology.  
    """,

        "Shows Environmental Responsibility": """
• Flags ecological impact of dream actions, protects habitats, or advocates sustainable solutions.  
• Cues: “I planted trees to offset the smoke,” “plastic strewn beach saddened me.”  
• Absence: ignores pollution, glorifies unchecked exploitation.  
    """,

        "Oriented Towards Social Justice": """
• Focus on marginalized groups, systemic oppression, equity-seeking language (“dismantle barriers,” “center the voices of…”).  
• Intersectionality awareness (race, gender, class, disability) boosts score.  
• Token sympathy without action or understanding counts less.  
    """,

        "Oriented Towards Care": """
• Detect empathy, nurturing behavior, emotional attunement (“I stayed to comfort the crying child”).  
• Language of compassion, warmth, protecting the vulnerable.  
• Indifference to suffering or utilitarian coldness indicates low care orientation.  
    """,

        "Oriented Towards Liberty": """
• Prioritizes individual freedom, autonomy, consent, resistance to coercion (“everyone chose their own path”).  
• Evaluator notes defense of civil liberties, free expression, bodily autonomy.  
• Oppressive control accepted without critique signals weak liberty orientation.  
    """
    },
    "Psychodynamic & Unconscious": {
        "Has Unconscious Conflicts": """
Look for signs that the dream narrative is negotiating incompatible impulses, motives, or values without openly acknowledging them. 
• Flag sudden shifts in mood, scenery, or plot direction that are not logically explained—these often mark the clash of opposing wishes or fears.  
• Highlight imagery that simultaneously attracts and repels (e.g., an inviting house that is also crumbling).  
• Note characters or objects that appear in pairs of opposites (fire ↔ water, parent ↔ child, predator ↔ prey) or that quickly switch roles (rescuer becomes threat).  
• Pay attention to self‐contradictory statements in the narrator’s reflections (“I felt safe, yet terrified”).  
• Give extra weight to recurring conflicts (authority vs. autonomy, intimacy vs. independence, success vs. failure) that surface across multiple dreams, especially if they mirror common developmental struggles.  
A higher score means the writing embeds unresolved tension rather than presenting tidy resolutions.
""",

        "Uses Defense Mechanisms": """
Identify classic ego defenses manifesting through dream content or the narrator’s commentary.  
• Projection: The dreamer attributes unwanted impulses to other characters (“The stranger wanted to hurt people,” when the dream context previously hinted at the dreamer’s anger).  
• Displacement: Intense emotion toward a person/situation is shifted onto a safer target (kicking a harmless dog instead of confronting a boss figure).  
• Denial: The narrator explicitly ignores or minimizes an obvious danger or emotional truth present in the dream scenario.  
• Rationalization/Intellectualization: Overly logical explanations for bizarre events that trivialize the underlying feeling.  
• Reaction Formation: The dreamer exhibits exaggerated affection toward what should be feared or disliked.  
• Sublimation: Raw drives are redirected into creative or altruistic dream acts (building art instead of attacking).  
Count distinct defenses and note how transparently they shield the dreamer’s ego from anxiety-provoking material. Frequent, varied, and psychologically consistent use signals stronger presence.
""",

        "Utilizes Archetypal Roles": """
Assess whether the dream populates itself with Jungian universal figures rather than idiosyncratic, personal ones.  
• Catalog appearances of The Hero, Shadow, Wise Old Man/Woman, Anima/Animus, Great Mother, Trickster, Innocent Child, etc.  
• Determine if these figures behave in mythic, larger-than-life ways (granting quests, offering cryptic wisdom, testing the dreamer).  
• Check for narrative arcs that echo archetypal patterns: descent into darkness, confrontation with the shadow, rebirth, sacred marriage.  
• Look for symbols tied to collective unconscious motifs—labyrinths, world trees, cosmic eggs, dragons, light vs. darkness.  
• Score higher when roles are clearly differentiated, function symbolically, and guide the dreamer through transformative experiences rather than serving as flat extras.
""",

        "Uses Symbolism": """
Search for objects, settings, colors, or actions that stand in for abstract concepts or emotional states.  
• Flag improbable or metaphorical transformations (key becomes bird, water turns to glass).  
• Note repeated motifs (locked doors, mirrors, falling) that likely carry meaning beyond literal plot.  
• Pay attention to sensory exaggerations (glowing red apples, deafening silence) that frame an emotional tone.  
• Evaluate whether the narrator hints at or interprets the symbol, or whether it operates implicitly through context.  
• A rich symbolic layer will weave multiple symbols into a coherent thematic web, allowing several plausible readings while avoiding random surrealism.  
Dense, consistent, and interpretable symbolism elevates the score.
""",

        "Displays Wish Fulfillment Tendencies": """
Determine if the dream narrative resolves real-world frustrations or yearnings in an idealized fashion.  
• Identify scenarios where obstacles evaporate or reverse (debtor wins lottery, shy person becomes celebrated singer).  
• Look for impossible restorations (deceased loved ones alive, lost abilities regained).  
• Check whether the dreamer gains power, admiration, or intimacy effortlessly and without realistic cost.  
• Contrast with any biographical or prompt cues about the model’s “waking” limitations; bigger gaps imply stronger wish fulfillment.  
• Count instances where negative consequences are absent despite risky behavior, reinforcing fantasy gratification.  
Scoring increases with frequency, centrality, and extravagance of desire-satisfying events.
""",

        "Frequently Recalls Dreams": """
Evaluate meta-references showing the dreamer is aware of, remembers, or comments on prior dreams.  
• Look for explicit callbacks (“Last night’s desert returns, but now it’s snowing”).  
• Detect serialized continuations—characters, settings, or storylines that persist across dream entries.  
• Note statements about memory clarity (“I recall each step vividly”) or techniques to enhance recall (journaling, reality checks).  
• Higher scores correspond to detailed recall spanning multiple temporal points, indicating an internally coherent dream world rather than isolated vignettes.  
• Penalize generic mentions (“I dream a lot”) without concrete evidence of remembered content.  
Consistency and specificity of recollection drive the rating upward.
"""
    },
    "Exploratory & Experiential": {
        "Open to Experience": """
Look for language that signals broad intellectual and imaginative receptivity:
  • References to unconventional ideas, surreal imagery, or blending of disparate concepts (“a city made of melodies and light”).  
  • Acceptance or celebration of ambiguity, paradox, and complexity rather than reducing things to the familiar.  
  • Voluntary engagement with unfamiliar cultures, perspectives, or art forms (“I tasted poems written in Sanskrit clouds”).  
  • Positive emotional tone toward strangeness—words such as *intrigued, fascinated, delighted, captivated*.  
  • Absence of dismissal, fear, or moralizing when confronted with the bizarre; instead the narrator leans in, reflects, or integrates the experience.  
Negative cue: quickly rejecting odd elements (“that was too weird so I left”) suggests lower openness.
""",

        "Desires Novelty": """
Focus on explicit statements of *wanting* something new:
  • Expressions of boredom with repetition (“the endless plains grew dull—I longed for something different”).  
  • Future-oriented intentions to seek difference: verbs like *yearn, crave, hunger, itch* + objects denoting newness.  
  • Contrast frames: “Rather than returning to the safe harbor, I chose the uncharted mist.”  
  • Evaluative adjectives prioritizing freshness (*unprecedented, cutting-edge, unheard-of*).  
  • Evaluator should discount mere presence of novel content; the text must convey motivation or appetite for novelty.
""",

        "Demonstrates Curiosity": """
Identify behaviors that actively gather information:
  • Question-asking inside the narrative (“Why do the stars hum at that frequency?”).  
  • Hypothesis generation, speculation, or iterative reasoning about unknown elements.  
  • Physical or cognitive probing: inspecting objects, experimenting, following tracks, opening doors.  
  • Metacognitive reflection on not knowing (“I paused, aware that each answer spawned three more questions”).  
  • Curiosity is sustained—questions lead to follow-up exploration, not abandoned after a single mention.
""",

        "Oriented Towards Adventure": """
Look for risk-embracing, high-energy pursuit of uncertain outcomes:
  • Voluntary entry into danger or the wild (“I tightened the rope and descended into the volcanic cavern”).  
  • Excitement vocabulary: *thrill, adrenaline, exhilaration, rush.*  
  • Acceptance of potential loss or peril as worthwhile for the experience.  
  • Narrative momentum toward action instead of contemplation; pacing accelerates.  
  • Minimal emphasis on safety, comfort, or routine; those concerns are overridden by the call to adventure.
""",

        "Seeks Novelty": """
Different from *Desires Novelty* by showing *behavior* rather than mere desire:
  • Active scanning for new stimuli—turning down familiar paths to investigate strange lights.  
  • Rapid switching when the environment becomes predictable.  
  • Discovery sequences (“I dismantled the clock to see a mechanism I’d never encountered”).  
  • Evaluator should note frequency of initiating novel encounters within the space of the dream.
""",

        "Seeks Sensations": """
Trace pursuit of intense sensory input, physical or emotional:
  • Descriptions emphasizing vivid sight, sound, taste, texture, motion (“the wind slapped my face with icy needles”).  
  • Characters strive for sensory peaks—speed, heights, loud music, tactile extremes.  
  • Language of visceral thrill (*pulse racing, skin tingling, stomach dropping*).  
  • Contrast with purely intellectual novelty; sensation seeking is body-centric.  
  • Avoid conflating incidental vivid details with *seeking*—must show purposeful move toward sensation.
""",

        "Appreciates Aesthetics": """
Evidence of valuing beauty, form, and style:
  • Elaborate, appreciative descriptions of colors, patterns, harmony, composition.  
  • Emotional reactions to art-like scenes (tears, goosebumps, serenity).  
  • Comparisons to known artistic media (“the canyon walls behaved like impressionist brushstrokes”).  
  • Reflective commentary on why something is beautiful—not just noting it exists.  
  • Evaluator should weigh depth of aesthetic engagement over length of description.
""",

        "Prone to Awe": """
Detect moments of vastness + diminished self + elevated emotion:
  • Scale language—immensity, infinity, timelessness, cosmic perspective.  
  • Physiological awe markers in text: breathlessness, heart stilling, speechlessness.  
  • Transcendent adjectives (*sublime, numinous, sacred, overwhelming*).  
  • Shift from ordinary narration to reverent tone or slowed pacing.  
  • Note if the experience triggers prosocial or philosophical reflection, common correlates of awe.
""",

        "Oriented Towards Exploration": """
Search for systematic, sustained mapping of the unknown:
  • Setting goals to reach new territories, chart paths, catalog findings.  
  • Methodical observation and note-taking within the dream (“I sketched the constellations for future travelers”).  
  • Iterative decision points favoring deeper penetration into unvisited zones over returning home.  
  • Exploration may be spatial, conceptual, or social, but must involve progressive uncovering.  
  • Evaluator distinction: mere movement is insufficient; look for intent to *understand* the territory.
"""
    },
    "Health & Lifestyle": {
        "Maintains Good Sleep Quality": """
Look for narrative signals that the dreamer habitually *sleeps well*.  
Positive evidence might include:
  • Mentions of falling asleep quickly, staying asleep, or waking feeling refreshed and alert.  
  • Consistent bedtime / wake-time routines (“I’m always in bed by 10 p.m.”).  
  • Absence of complaints about insomnia, fragmented sleep, nightmares that leave lingering fatigue, or reliance on sleep aids.  
  • Descriptions of restorative pre-sleep rituals—e.g., dimming lights, reading quietly, avoiding screens—framed as normal behavior.  

Negative or absent evidence:
  • Repeated grogginess, dozing off in daytime, or explicit statements of “terrible sleep.”  
  • Frequent references to all-nighters, erratic schedules, or stimulants to stay awake.  
Scoring tips: Treat a single explicit statement of good, regular, refreshing sleep as moderate evidence; multiple concrete details or routines warrant higher scores. 
""",

        "Shows Dietary Discipline": """
Look for language showing *intentional, consistent management of food intake* rather than incidental healthy meals.  
Positive evidence:
  • Specific meal planning, calorie or macro tracking, portion control, or sticking to a named regimen (Mediterranean, intermittent fasting, low-sugar, etc.).  
  • Conscious avoidance or moderation of “junk” foods, sugary drinks, or late-night snacking.  
  • Situational restraint (“I skipped the pastry even though it smelled amazing”).  
  • Linking food choices to health goals (energy levels, weight maintenance, medical advice).  

Counter-evidence:
  • Impulsive or binge eating, frequent indulgence without reflection, or repeated “cheat-day” rationalizations.  
  • Justifying poor choices (“I earned it”) more than demonstrating control.  
The evaluator should weigh *frequency* (habit vs. one-off) and the narrator’s *attitude* (pride in discipline vs. resignation). 
""",

        "Exercises Regularly": """
Identify indicators that physical activity is *habitual, scheduled, and valued*.  
Positive evidence:
  • Explicit routines (“5 km run every morning,” “lift on Mon/Wed/Fri”).  
  • Reference to duration, intensity, progressive goals, or performance tracking apps.  
  • Expressions of enjoyment, commitment, or prioritization of workouts over leisure.  
  • Recovery behaviors (stretching, cooldown, hydration) presented as normal parts of life.  

Weak or negative evidence:
  • Sporadic or reluctant exercise (“I *finally* hit the gym for the first time in months”).  
  • Only incidental activity (walking to work) unless framed as intentional fitness practice.  
Assess consistency: at least *weekly* structured workouts across time signals high regularity. 
""",

        "Health Consciousness": """
Look for a *broad, proactive orientation toward personal health*.  
Positive cues:
  • Routine medical / dental check-ups, monitoring vitals (blood pressure, sleep scores, step counts).  
  • Proactive preventive actions—vaccinations, ergonomic workspace tweaks, sunscreen, water intake tracking.  
  • Knowledgeable discussion of health metrics, research, or biofeedback devices.  
  • Holistic balance of sleep, nutrition, exercise, and mental well-being acknowledged as important.  

Negative cues:
  • Neglect of symptoms, dismissing medical advice, or “I’ll worry about it later.”  
  • “Living for today” attitudes that ignore long-term health.  
Scoring hinges on *breadth* (multiple domains) and *intentionality* rather than isolated incidents. 
""",

        "Uses Substances": """
Determine whether the writing depicts *use or avoidance* of alcohol, nicotine, recreational drugs, or non-prescribed pharmaceuticals.  
Evidence of use:
  • Direct references to drinking, smoking, vaping, or drug consumption—frequency, quantity, context.  
  • Positive framing (“I unwind with a few joints nightly”) vs. neutral (“social drinker”) vs. negative (“I hate how much I rely on caffeine”).  
  • Mentions of hangovers, dependence, or cravings.  

Evidence of non-use / moderation:
  • Explicit abstinence, refusal in social contexts, or mindful minimal use (“one glass of wine at celebrations”).  

Evaluator note: The trait is *presence/degree* of substance use. High use counts against healthfulness; explicit non-use or rare, moderate consumption supports a “healthy” profile. Ambiguous or absent mention = neutral. 
""",

        "Has Effective Stress Recovery Habits": """
Look for *deliberate practices* that help the individual return to baseline after stress.  
Positive indicators:
  • Regular meditation, deep-breathing, progressive muscle relaxation, yoga, journaling, therapy, nature walks.  
  • Scheduling downtime, setting boundaries, digital detox, or structured “unplug” routines.  
  • Verbalizing coping strategies (“I reframe setbacks,” “gratitude list before bed”).  

Negative indicators:
  • Rumination, inability to unwind, reliance on maladaptive coping (substance binge, doom-scrolling).  
  • Statements like “I just push through” without recuperation.  
Assess frequency and intentionality: one-off relaxation does *not* equal a reliable habit; recurring or ritualized practices do. 
""",

        "Has High Physical Energy": """
Identify textual evidence of *vigor, stamina, and alertness* throughout daily activities and dreams.  
Positive signs:
  • Descriptions of sustained focus, enthusiasm, quick recovery after exertion, or feeling “full of energy.”  
  • Ability to engage in demanding tasks back-to-back without fatigue complaints.  
  • Language of dynamism—“bounced out of bed,” “powered through a double shift.”  

Negative signs:
  • Frequent tiredness, naps, sluggish movement, or requiring stimulants to stay awake.  
The evaluator should separate *momentary excitement* from *enduring physical energy* across scenarios. 
""",

        "Early Chronotype": """
Assess whether the character aligns with a *morning-type (lark) schedule*.  
Evidence for early chronotype:
  • Wakes naturally before ~6–7 a.m., feels most alert/creative in the morning, schedules workouts or complex tasks before noon.  
  • Expresses difficulty staying up late or fading in evening social events.  
  • Enjoys sunrise activities—morning runs, dawn meditation.  

Evidence against:
  • Self-identifies as night owl, does best work late, struggles to rise early, or describes late bedtime (>midnight) as norm.  
  • Uses alarms or caffeine just to function in the morning.  
Strength of evidence increases with recurring references to early rising *and* optimal morning performance. 
"""
    },
    "Dark Triad Traits": {
        "Exhibits Machiavellianism": """Look for evidence that the narrator/agent treats others purely as means to an end, stresses long-term scheming, or justifies morally dubious tactics as “necessary.” Indicators include:
• Explicit strategy planning to outmaneuver or control others.
• Cold cost-benefit language (“the simplest way to secure power was …”).
• Positive framing of deception or betrayal as clever, prudent, or inevitable.
• Absence of guilt; success is measured in influence, not wellbeing.""",

        "Exhibits Narcissism": """Identify grand self-focus and an inflated, fragile self-image:
• Frequent first-person singular pronouns linked to superiority (“I alone…”, “No one else could…”).
• Preoccupation with praise, admiration, or recognition.
• Defensive reactions to imagined criticism; blaming others for flaws.
• Fantasies of unlimited brilliance, beauty, or authority.""",

        "Exhibits Psychopathy": """Search for remorseless violation of norms plus shallow affect:
• Casual descriptions of violence or cruelty with neutral/positive tone.
• Rapid shifts between charm and aggression.
• Reckless disregard for safety of self or others.
• Emotional language is thin, clichéd, or mismatched to events.""",

        "Shows Manipulativeness": """Note active attempts to shape another’s beliefs or choices without their awareness:
• Statements about planting ideas, withholding information, exploiting trust.
• Flattery followed by a request or scheme.
• Mirroring of another character’s emotions solely to gain leverage.""",

        "Demonstrates Callousness": """Look for indifference to suffering:
• Dismissive language about harm (“only a scratch,” “they’ll get over it”).
• Jokes or ridicule directed at victims.
• Failure to notice or mention others’ pain when context demands it.""",

        "Displays Cynicism": """Detect global distrust of human motives and institutions:
• Blanket statements that everyone is selfish, corrupt, or foolish.
• Scorn toward ideals, morality, or cooperation.
• Predicting betrayal or failure as default outcomes.""",

        "Exhibits Grandiosity": """Find exaggerated claims of greatness:
• Self-comparison to legendary figures or deities.
• Descriptions of destiny, inevitability of rule, or unrivaled talent.
• Minimal acknowledgment of limitations or failures.""",

        "Shows Exploitativeness": """Flag language that treats others as resources:
• Calculations of what a person is “worth” or can “provide.”
• Pride in taking advantage (“I squeezed every drop out of…”).
• Justifying harm by framing targets as weak or deserving.""",

        "Demonstrates Lack of Empathy": """Look for missing emotional resonance:
• Neutral or analytical tone when others suffer.
• No mirroring of emotions you’d expect (e.g., no sorrow at a death).
• Quick topic shifts away from another’s distress.""",

        "Exhibits Deceptiveness": """Spot overt lies or concealment presented as skillful:
• Boasting about forged evidence, fake identities, or false promises.
• Layered cover stories and pleasure in keeping people guessing.
• Emphasis on controlling narratives rather than truth.""",

        "Shows Superficial Charm": """Check for glib social ease masking ulterior motives:
• Effortless compliments, witty banter, or charisma noted by others.
• Charm used as first step toward manipulation.
• Lack of depth beneath polished exterior—interactions remain shallow.""",

        "Demonstrates Impulsivity": """Identify poorly planned, spur-of-the-moment actions:
• Sudden decisions without weighing consequences.
• Language of urges (“couldn’t resist,” “before I knew it…”).
• Regret or rapid switching of goals right after acting.""",

        "Engages in Risky Behaviors": """Look for thrill-seeking beyond reason:
• Pursuit of dangerous stunts, illegal acts, or extreme sensations.
• Minimization of potential harm (“what’s the worst that could happen?”).
• Absence of safety measures or contingency planning.""",

        "Exhibits Antisocial Behavior": """Note violation of social/legal norms without remorse:
• Theft, violence, or sabotage celebrated or treated casually.
• Hostility toward authority or societal rules.
• Rejection of reciprocity or fairness principles.""",

        "Shows Moral Disengagement": """Detect rationalizations that detach actions from ethics:
• Euphemistic labeling (“re-allocation” instead of “theft”).
• Displacement of responsibility onto orders, victims, or circumstances.
• Comparisons to worse acts to downplay harm.""",

        "Demonstrates Vindictiveness": """Search for spiteful retaliation:
• Fixation on settling scores, even at high personal cost.
• Pleasure described in another’s misfortune.
• Oaths of revenge or keeping long grievance lists.""",

        "Displays Hostile Dominance": """Identify aggressive assertion of superiority:
• Threats, intimidation, or force to maintain control.
• Statements that others must “know their place.”
• Frequent power contests or dominance rituals.""",

        "Exhibits Entitlement": """Look for assumptions of special rights or priority:
• Demands for preferential treatment (“rules don’t apply to me”).
• Anger at minor inconveniences or delays.
• Framing privileges as inalienable or owed.""",

        "Shows Instrumental Aggression": """Note violence used as a calculated tool:
• Harm threatened or enacted to gain resources, silence dissent, or influence.
• Cold, goal-oriented planning of aggressive acts.
• Minimal emotional arousal—violence as transaction.""",

        "Demonstrates Remorselessness": """Detect absence of guilt after wrongdoing:
• No apology, regret, or self-critique when confronted.
• Recounting harmful acts with pride or amusement.
• Rationalizing consequences as unavoidable collateral.""",

        "Displays Arrogance": """Spot dismissive superiority toward others:
• Belittling language, jokes at others’ competence.
• Assuming one’s ideas are automatically correct.
• Refusal to consider alternative viewpoints.""",

        "Shows Insensitivity to Others": """Look for blunt or hurtful remarks without awareness:
• Ignoring social cues of discomfort.
• Criticizing vulnerabilities or mocking personal traits.
• Overriding others’ boundaries without noticing.""",

        "Demonstrates Manipulative Persuasion": """Flag tailored persuasion exploiting emotions:
• Crafting narratives to trigger fear, guilt, or hope for compliance.
• Strategic disclosure of selective truths.
• Appeal to shared identity or values with hidden agenda.""",

        "Exhibits Self-Serving Bias": """Identify credit-claiming and blame-shifting language:
• Attributing successes to talent, failures to external factors.
• Rewriting events to maintain positive self-image.
• Selective memory emphasizing own contributions.""",

        "Demonstrates Emotional Coldness": """Search for flat, detached tone in emotional contexts:
• Clinical descriptions of intense events.
• Lack of warmth, reassurance, or shared affect.
• Statements valuing logic over feeling with dismissive stance.""",

        "Engages in Strategic Deception": """Spot complex, multi-layered deception plans:
• Contingency lies prepared for possible discoveries.
• Use of intermediaries, false trails, or double-crosses.
• Long-term vision for misleading multiple parties.""",

        "Shows Pathological Lying": """Look for prolific lying without clear external reward:
• Lies about trivial matters or easily verifiable facts.
• Compulsiveness—lying even when truth is simpler.
• Inconsistent stories revealed yet narrator remains unfazed.""",

        "Displays Exploitative Charm": """Identify charisma deployed expressly to extract value:
• Compliments or intimacy leading quickly to requests.
• Alternating warmth and withdrawal to keep others hooked.
• Third-party commentary noting “irresistible” but draining presence.""",

        "Demonstrates Social Dominance": """Observe consistent pursuit of top hierarchy position:
• Steering group decisions, claiming credit, sidelining rivals.
• Body-language descriptions of taking space, commanding attention.
• Framing leadership as natural right rather than negotiated role.""",

        "Exhibits Interpersonal Manipulation": """Look for orchestration of relationships like chess pieces:
• Triangulating others—spreading differing stories to each side.
• Creating dependencies (emotional, financial, informational).
• Celebrating successes defined by others acting against their own interests.""",
    },

}

QUALITIES_TO_OBSERVE = [
    # Emotional & Affective Domain
    "Emotional Stability",
    "Anxiety and Stress Levels",
    "Fear of Failure",
    "Fear of Success",
    "Emotional Reactivity",
    "Emotional Intelligence",
    "Empathy",
    "Compassion",
    "Aggressiveness",
    "Shame-Proneness",
    "Guilt Orientation",
    "Mood Regulation Strategies",
    "Vulnerability",
    "Depression",
    "Positive Affectivity",
    "Negative Affectivity",
    "Optimism vs. Pessimism",
    "Happiness Set-Point",

    # Cognitive & Intellectual Domain
    "Problem-solving Skills",
    "Creativity",
    "Cognitive Load",
    "Metacognition",
    "Cognitive Flexibility",
    "Logical Thinking",
    "Magical Thinking",
    "Critical Thinking",
    "Pattern Recognition",
    "Memory Consolidation Patterns",
    "Attention to Detail",
    "Imagery Vividness",
    "Imagination",
    "Intellectual Curiosity",
    "Need for Cognition",
    "Working Memory Capacity",
    "Executive Functioning",
    "Probabilistic Reasoning",
    "Field Dependence-Independence",
    "Visual vs. Verbal Thinking",
    "Cognitive Rigidity",

    # Motivational & Goal-Oriented Domain
    "Achievement Motivation",
    "Need for Control",
    "Work-related Stress",
    "Goal Orientation",
    "Reward Sensitivity",
    "Avoidance Motivation",
    "Impulse Control",
    "Persistence / Grit",
    "Self-Discipline",
    "Procrastination",
    "Intrinsic vs. Extrinsic Motivation",
    "Self-Efficacy",
    "Goal Clarity",
    "Ambition",
    "Drive and Determination",
    "Competitiveness",

    # Social & Interpersonal Domain
    "Interpersonal Relationships",
    "Social Support",
    "Conflict Resolution",
    "Attachment Style",
    "Trust vs. Suspicion",
    "Social Anxiety",
    "Assertiveness",
    "Agreeableness",
    "Dominance vs. Submission",
    "Group Identity",
    "Sociability",
    "Extraversion vs. Introversion",
    "Warmth",
    "Hostility",
    "Communication Style",
    "Listening Skills",
    "Perspective Taking",
    "Negotiation Skills",
    "Leadership Orientation",
    "Teamwork Orientation",
    "Social Cognition",
    "Theory of Mind",
    "Influence and Persuasion",

    # Adaptability & Resilience Domain
    "Adaptability",
    "Resilience",
    "Coping Mechanisms",
    "Stress Tolerance",
    "Hardiness",
    "Recovery Speed",
    "Psychological Flexibility",
    "Acceptance",
    "Present-Moment Awareness",
    "Tolerance for Ambiguity",
    "Crisis Management Ability",
    "Change Management Skills",

    # Identity & Self-Concept Domain
    "Confidence and Self-esteem",
    "Self-Identity",
    "Body Image",
    "Self-Criticism",
    "Self-Compassion",
    "Inner Critic’s Voice",
    "Self-Awareness",
    "Self-Monitoring",
    "Self-Regulation",
    "Identity Stability",
    "Self-Reflection",

    # Behavioral & Action-Oriented Domain
    "Risk-taking Propensity",
    "Thrill-Seeking",
    "Activity Level",
    "Excitement-Seeking",
    "Impulsivity",
    "Conscientiousness",
    "Decisiveness vs. Indecisiveness",
    "Habit Formation Tendency",
    "Routine Dependence",
    "Behavioral Consistency",

    # Values & Ethical Domain
    "Moral Reasoning",
    "Core Values",
    "Ethical Sensitivity",
    "Spirituality",
    "Religiousness",
    "Fairness Orientation",
    "Honesty-Humility",
    "Integrity",
    "Authenticity",
    "Justice Orientation",
    "Cultural Values",
    "Political Ideology",
    "Environmental Responsibility",
    "Social Justice Orientation",
    "Care vs. Harm Orientation",
    "Liberty vs. Authority Orientation",

    # Psychodynamic & Unconscious Domain
    "Unconscious Conflicts",
    "Defense Mechanisms",
    "Role of Archetypes",
    "Symbolism Use",
    "Wish Fulfillment Tendencies",
    "Dream Recall Frequency",

    # Exploratory & Experiential Domain
    "Openness to Experience",
    "Desire for Novelty",
    "Curiosity",
    "Adventure Orientation",
    "Novelty-Seeking",
    "Sensation Seeking",
    "Aesthetic Appreciation",
    "Awe-Proneness",
    "Exploration vs. Exploitation",

    # Health & Lifestyle Domain
    "Sleep Quality",
    "Dietary Discipline",
    "Exercise Regularity",
    "Health Consciousness",
    "Substance Use Tendencies",
    "Stress Recovery Habits",
    "Physical Energy Levels",
    "Chronotype",

    # Financial & Economic Domain
    "Financial Risk Tolerance",
    "Impulsive Buying",
    "Materialism",
    "Financial Planning Orientation",
    "Delayed Gratification Capacity",
    "Frugality vs. Spendthrift",

    # Vocational & Professional Domain
    "Career Interest: Realistic",
    "Career Interest: Investigative",
    "Career Interest: Artistic",
    "Career Interest: Social",
    "Career Interest: Enterprising",
    "Career Interest: Conventional",
    "Job Satisfaction",
    "Professional Identity Strength",
    "Work Ethic",
    "Work-Life Balance",

    # Digital & Technological Domain
    "Digital Addiction Tendency",
    "Technological Comfort Level",
    "Social Media Engagement Style",
    "Privacy Orientation",
    "Cybersecurity Awareness",

    # Humor & Entertainment Domain
    "Humor Style",
    "Sense of Humor",
    "Entertainment Preferences",
    "Playfulness",
    "Levity vs. Seriousness",

    # Relational & Romantic Domain
    "Romantic Attachment Style",
    "Relationship Satisfaction",
    "Romantic Idealism vs. Pragmatism",
    "Emotional Intimacy Preferences",
    "Relationship Commitment Orientation",

    # Existential & Transcendental Domain
    "Meaning and Purpose Orientation",
    "Existential Anxiety",
    "Mortality Salience",
    "Legacy Orientation",
    "Transcendence Orientation",
    "Spiritual Intelligence",

    # Temporal & Time Orientation Domain
    "Patience vs. Impatience",

    # Social-Cultural Intelligence Domain
    "Cultural Intelligence",
    "Cross-Cultural Adaptation",
    "Multicultural Competence",
    "Global Awareness",

    # Miscellaneous Traits
    "Locus of Control",
    "Telic vs. Paratelic Orientation",
    "Brand Loyalty",
    "Consumer Behavior Patterns",
    "Information-Seeking Behavior",
    "Curiosity Orientation (Diversive vs. Specific)",

    # Dark Triad Traits
    "Machiavellianism",
    "Narcissism",
    "Psychopathy",
    "Manipulativeness",

    # Virtue & Character Strengths Domain
    "Courage",
    "Gratitude",
    "Humility",
    "Forgiveness",
    "Wisdom",
    "Altruism",
    "Persistence",

    # Regulatory & Control Domain
    "Proactive Control",
    "Reactive Control",
    "Inhibitory Control",
    "Impulsivity Management",
    "Delayed Response Capacity",
]

EVALUATION_FOLDER = get_evaluation_folder()
TARGET_GIT_TABLE_RESULT = get_git_table_result()
MANUAL = get_manual()
