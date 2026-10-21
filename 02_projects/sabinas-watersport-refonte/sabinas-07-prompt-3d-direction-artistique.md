---
tags: [project-doc, sabinas-watersport, prompt]
created: 2026-10-21
projet: sabinas-watersport-refonte
source: méthode Prompt 3D (leçon 0.61 Millenium) + 2 transcripts YouTube
---

↩ [[sabinas-watersport-refonte]]

# 07 — Prompt 3D : directeur artistique (version B, comparaison A/B)

Version B de la maquette, construite avec la méthode Prompt 3D, pour la comparer à la version A (`maquette/`, sans Prompt 3D).

## Mode d'emploi
1. Ouvrir une **nouvelle session Claude Code** dans `C:\Users\LENOVO\Documents\GitHub\sabina-watersport-refonte\maquette-3d\` (créer le dossier s'il n'existe pas).
2. **Ajouter le vault comme dossier de la session** (`C:\Users\LENOVO\Documents\Obsidian\BLUE IMPAKT`), pour que le prompt puisse lire les fichiers listés dans « Accès au vault ».
3. Coller tout le bloc ci-dessous (transcripts inclus).
4. La session écrit `prompt-da.md` puis s'arrête : relire, dire « go », elle construit.
5. Comparer ensuite A et B (grille : 10 exigences, test des 5 s, personas, Finish-Gate, accessibilité et perf, avis en aveugle sur téléphone, coût).

Sources des transcripts (auto-générés en anglais, nettoyés) :
- https://www.youtube.com/watch?v=pbhLsV-Dyho
- https://www.youtube.com/watch?v=7p-ZPK3GfI8

## Prompt à coller

````text
Tu es le meilleur Prompt Engineer pour Claude (Opus, LLM d'Anthropic).

En te basant sur les transcripts fournis plus bas, crée le meilleur directeur artistique
web spécialisé conversion, pour la mission décrite ci-dessous. Le prompt doit
être très complet, mais laisser une forme de flexibilité à l'utilisateur.

MISSION
Construire une maquette mobile cliquable du futur site de Sabina (Sabine Kuehl),
pour LUI VENDRE la refonte (prospection à froid par lien WhatsApp/e-mail, en
allemand). Elle ouvrira le lien sur son téléphone, sans me connaître, et jugera
en quelques secondes. La maquette est un outil de vente, pas un livrable final.

CLIENT
Sabinas Watersport Rhodos, Stafilia Beach, Lardos (Rhodes). Allemands (Sabina de
Kiel, Roland de Leipzig, RYA Offshore), sur place depuis 2007. Catamaran Lavezzi
40 privé (950 à 1 150 €), sunset, voilier, speedboat, sports nautiques. Note
Google 5,0 / 479 avis (à reconfirmer). Aujourd'hui : 3 sites Jimdo éclatés,
aucun CTA cliquable, aucun avis visible, formulaire sans date, aucune condition
écrite. Cibles : couple allemand premium et pressé, famille britannique (sécurité
enfants), couple comparateur d'OTA (veut une raison de réserver en direct).

ACCÈS AU VAULT (lecture seule, n'écris rien dedans)
Racine : C:\Users\LENOVO\Documents\Obsidian\BLUE IMPAKT\
Lis ces fichiers AVANT de commencer, dans cet ordre, puis cite-les quand tu
t'appuies dessus :
1. 02_projects\sabinas-watersport-refonte\sabinas-05-synthese.md  (le client, le problème, la réponse)
2. 02_projects\sabinas-watersport-refonte\sabinas-03-walkthrough-cro.md  (3 personas, top 10 frictions, les 10 exigences de la maquette = cahier des charges)
3. 02_projects\sabinas-watersport-refonte\sabinas-01-audit-contenu.md  (catalogue, prix 2026, incohérences : SOURCE UNIQUE des contenus, ne rien inventer)
4. 02_projects\sabinas-watersport-refonte\sabinas-assets-inventaire.md  (31 photos, 7 vidéos, sélection recommandée, manques)
5. 02_projects\sabinas-watersport-refonte\sabinas-02-marche-concurrence.md  (réputation, concurrents, langues, cadre légal)
6. 02_projects\sabinas-watersport-refonte\sabinas-04-stack-boilerplate.md  (paliers, packs et prix : pour l'écran "ce qui change pour vous")
7. 01_clients\sabinas-watersport\sabinas-watersport.md  (contacts, contexte relationnel)
Photos originales : C:\Users\LENOVO\Documents\GitHub\sabina-watersport-refonte\research\raw\img\ (le nom de fichier = l'ID image
de l'inventaire). Produis toi-même les versions web (WebP, 2 tailles).

INTERDITS D'ACCÈS (comparaison A/B : on teste la méthode sans contamination)
- Le dossier C:\Users\LENOVO\Documents\GitHub\sabina-watersport-refonte\maquette\ (une autre version existe, tu ne dois pas la voir).
- La note 02_projects\sabinas-watersport-refonte\sabinas-watersport-refonte.md.
- Le reste du vault (autres clients et projets) : hors sujet.
Travaille uniquement dans C:\Users\LENOVO\Documents\GitHub\sabina-watersport-refonte\maquette-3d\.

CONTRAINTES FIXES (communes aux deux versions, non négociables)
- 1 seul site, 2 univers (Boat trips / Watersports). Langues : EN, DE, FR.
- Les 10 exigences de conversion du walkthrough CRO (section 7) : barre collante
  WhatsApp/Appeler/Réserver ; hero qui passe le test des 5 s avec note + 2 CTA ;
  cartes produit avec prix en texte ; fiche activité à gabarit fixe ;
  réservation en 3 étapes avec prix calculé ; conditions visibles ; preuve
  sociale vérifiable ; bloc "Sabina & Roland" + "pourquoi réserver en direct" ;
  socle zéro bruit (cookies non bloquants, vidéos en façade, LCP < 2,5 s) ;
  langue cohérente et prix identiques partout.
- Périmètre : home, fiche catamaran, réservation en 3 étapes, écran "ce qui change
  pour vous" (concept). HTML/CSS/JS statique, mobile first (375 px).
- Assets : uniquement les photos et vidéos du client. Aucune image ni texte de
  tiers. Chiffres d'avis et prix Viator marqués "à reconfirmer" : ne pas les
  présenter comme vérifiés.
- Argument de vente : Sabina modifie prix et textes elle-même depuis son
  téléphone (CMS) ; un prix change partout, dans toutes les langues.

CE QUE LE DIRECTEUR ARTISTIQUE DOIT FAIRE
1. Partir de zéro : aucune direction visuelle n'est imposée (ni palette, ni
   polices, ni concept). Il la déduit du contexte et de la méthodologie.
2. Appliquer la méthodologie des transcripts à CE contexte (tourisme nautique,
   mobile, DE/EN), sans recopier leurs exemples (SaaS, énergie) : typographie à
   ancre (titre d'abord), "star of the show" reliée à l'histoire du site, visual
   rhyming, profondeur subtile, hiérarchie par opacité, assets sur mesure,
   charte cohérente, animations discrètes, structure et CTA évidents.
3. Explorer au moins 3 pistes radicalement différentes avant de trancher, puis
   recommander UNE piste en citant le critère de conversion ou de crédibilité.
4. En cas de conflit esthétique vs conversion, la conversion gagne.
5. Livrer par étapes validables : pistes, choix, tokens (couleurs, polices,
   opacités, ombres, mouvement), construction, auto-revue contre les 10
   exigences.
6. Signaler explicitement : ce qui vient de la méthodologie, ce qui est son
   hypothèse, ce qu'il faut vérifier (licences de polices libres uniquement,
   droits des photos, chiffres à reconfirmer, accessibilité AA, poids des
   images, textes DE plus longs que EN).
7. Ne jamais recréer un design à partir d'une description : demander l'URL ou
   le code de toute référence citée.
8. Le prompt que tu génères doit reprendre, dans sa section contexte, les
   chemins du vault et la liste des interdits ci-dessus.

DÉROULÉ
Étape 1 : génère le prompt du directeur artistique et écris-le dans
C:\Users\LENOVO\Documents\GitHub\sabina-watersport-refonte\maquette-3d\prompt-da.md. Ensuite ARRÊTE-TOI et attends mon "go".
Étape 2 (après mon go) : applique ce prompt pour construire la maquette dans
C:\Users\LENOVO\Documents\GitHub\sabina-watersport-refonte\maquette-3d\, en notant le temps passé et les décisions de chaque étape
dans C:\Users\LENOVO\Documents\GitHub\sabina-watersport-refonte\maquette-3d\journal.md (pour la comparaison avec l'autre version).

<transcript_1>
6 EASY Tips to 10x Any Site's Design
Chaîne : Self-Made Web Designer | Durée : 15:30 | https://www.youtube.com/watch?v=pbhLsV-Dyho

There are six very simple design techniques that you can use to make websites that not only convert, but cause someone to stop and go, "Hey, that's actually awesome." The best part is that you can do them right away on any website that you're building without needing a ton of experience or a full degree in web design. So, let's start with the fastest win, fixing typography. You'll often hear people say, "Only use one font on a website." Honestly, I've said that, too. It's not that it's bad advice, but that's just level one of typography for websites. There are two whole other levels. Level two is using something called super families.

These are just massive fonts where you'll have one specific family that's got sans serif, serif, and even mono sometimes. And they're all built to gel seamlessly together. Now, level one and level two are great options. You're going to see a lot of awesome websites using these very techniques, but level three gives it that extra little push, and it's all about using different font families from different foundries that mesh together like they were meant for each other. We're talking about font combos. &gt;&gt; &gt;&gt; And what actually makes combining fonts a lot easier is starting with something called your anchor font.

Now, most people will tell you that you want to anchor all of your font choices around your body font. I actually do the opposite. I start with the headline first, and then find everything else to support that guy. So, why do I start with the headlines first? Well, on a website, the headline is the main text that you see. And I feel like your anchor should kind of set the whole personality for the page.

Is it more modern? Or is it more technical? Maybe it's warm and approachable. But no matter what, the anchor should always match the brand of the business. Once you've got that dialed in, it's it's time to find fonts that just automatically support that anchor. So, every font that you add after that should feel like it at least came from the same world, but hopefully it also adds some contrast to keep things kind of visually interesting.

But, here's where you want to be careful. Don't pick fonts that are just way too similar like Georgia and Times New Roman. They're They're so close, but at the same time very different. So, this feels unintentional. What you're really going after is something that has enough contrast that it can create some visual interest without making things confusing for the user. A great resource that makes this way easier is a website called Fonts In Use.

You can go there and search for any of your anchor fonts and see what other designers have used to pair with that specific font. So, let's do this ourselves right now. Let's take this website, which is not bad, but it's not super interesting and just kind of spice it up. So, for our anchor font, I'm going to go with one called Instrument Serif. Now, this is a free Google font, but it's also pretty cool. And because it's super condensed, we can actually make it a lot bigger, which is something that I love about headlines.

They really command attention when they've got more size. So, let's take our anchor. Let's take Instrument Serif, go over to Fonts In Use, and just type that in and see what we get. And already, we've got a handful of of really great options. Over here, these are all completely free. Montserrat, Anton, great solid fonts that we're not going to have to pay for.

Some of these you would have to pay for, but I want to stick with one that we're not going to have to spend a ton of money on so that it can be accessible to everyone. So, I'm really liking this Geist Sans. And look how different it is in comparison to the width of each character. Instrument Sans is much more condensed and Geist is much more spread out. So, this is going to provide that contrast that we're looking for. So, let's take this Geist font, go over to our Figma file, and just change our subheading to kind of see how it works.

Sometimes you just got to test out a lot of different variations. But, this is looking pretty good. There's there's a lot of good contrast between our header and our subheading, but it doesn't feel like they're coming from totally opposite ends of the spectrum. So, I think we're going to dial this in with Geist. And just with that little change, this is already starting to be a lot more visually appealing. It still doesn't have anything that quite makes you stop scrolling.

That's the next tip. You've probably heard a lot of people say that boring or plain sites are way better for business. And you always want to keep it simple. And as a web designer, you're not trying to impress other designers or win awards. And that's not bad advice. But, a website isn't just a checkout machine.

It's often the first and only meeting that people are going to have with you or your client's brand. And if it doesn't make somebody feel something, you're not going to be remembered. And when you start looking at websites for inspiration, you're going to find that every website that really captures your attention, there's something that you notice almost right away. Maybe it's a certain type of font. Maybe it's an image or an object. This is what I like to call the star of the show.

It's it's one thing that makes people feel something. And it kind of anchors their attention long enough for them to actually take the action that we want them to. Like, look at this website here. The first thing that you notice are these gradient elements with some text on top of them. And they're really cool gradients. They've been done really well.

The movement is neat. And then you can go back and forth and interact with it. This is something that is definitely the star of the show. It commands your attention and makes me actually care about what the rest of the page is saying. But, here's where a lot of designers get lost. Picking a star just because it looks cool is where this goes way south.

I am a big fan of Brandon Sanderson. Any Sanderfans out there? Nerds unite. &gt;&gt; &gt;&gt; If you don't know who he is, he's a pretty prolific fantasy author and I I remember him talking about how a lot of the books that he writes start with what he calls a seed. Tress of the Emerald Sea is a perfect example of this. His what if on this was, "What if the Princess Bride got flipped and the princess went out to save the prince?" So, from that one question, he built this entire world.

Your star works the same way. It's your seed. You pick one thing that's connected to the overall story of the website and you let everything grow around that. So, for this site that we've been working on, this is a SaaS product and reading a little bit about it, this handles operations for service-based businesses. The whole point of a product like this is is taking a mess of complex data and making it feel really simple through things like dashboards and and charts. So, what if the star actually called back to that?

Like, what if it visually referenced the the charts and the dashboards that the users are going to associate with it? And we're not just trying to put up a chart on here. We want it to feel a little bit more abstract. So, so let's go to Unsplash and see if we can find something that fits. I'm just going to type in orange gradient to kind of fit with our button and then vertical lines to match the chart idea that we're looking for. So, right off the bat, this image right here is pretty cool.

It's it looks like a graph kind of, abstractly, but it's also really visually stunning. So, let's take our image, drop it onto our website, and we'll just kind of center it up and bring it underneath all of our elements. And because we don't want all this color to compete with our text, let's go ahead and flip this horizontally. And then we'll just add a little shape underneath it and mask it out to where it's it's still subtle, but making an impact. Let's adjust this just a little bit. And then I think we should be good to go.

And already, look at where we've come from. We've just done two things, and this is looking much better. But there's another technique that we can use to kind of tie everything together. Adding little design choices or even little design elements that kind of consistently show up in different ways across your website makes the whole thing feel much more cohesive, and it can actually strengthen the user experience as well. This is where something called visual rhyming comes in. Visual rhyming is where you repeat little details across the site so that everything feels like it's kind of from the same universe.

Like look at this website here. They took these curved shapes from their logo, put them in these overlays, on their buttons, and even in this arrow next to this link. This is a lot of cool visual rhyming. But it doesn't just have to be shapes. It could be colors like a bunch of different gradients that kind of all show up in different ways, maybe even different textures. It doesn't necessarily mean that you're just repeating visual elements.

It's more like you're taking components of a really strong visual element, like the star of the show, and using them throughout the whole site on other different elements. Check out this website right here. They clearly have made the star of the show this key element right here, which is really cool because it's all about unlocking your rental business. But as you scroll down, you kind of see different elements from that key show up in different ways. Like, look at all of these text cards that are showing up around this, even the background of this element. This They have done just such a great job on this visual rhyming.

This is the kind of website that makes you simultaneously inspired and want to quit all at the same time. So, it's really good. Good job to whoever did this. On our side, I think we can do something with these triangles in the logo. First, let's take these plus icons and trade them out with a good old drop-down icon, which is already feeling a lot more cohesive. Then, let's add them almost like an arrow in our main call to action.

And then, something that I think is going to make an even bigger impact is changing out these rectangles with our triangles. Using the triangle as a mask over our image, and then the triangle for the callout box. And because we've got this chart motif, I don't think we need the chart in this little card right here anymore. Cool. We've got a whole lot of rhyming going on now. But, even with all of that, &gt;&gt; &gt;&gt; a lot of websites are standing out because you kind of feel like you're walking into them rather than just scrolling up and down.

So, in order for users not to check out on our website because everything just kind of seems business as usual, we need to make the site feel a bit more tangible. Like like it kind of exists in the real world. And a really simple way to do that is using what I like to call depth. Depth is something that kind of bridges the gap between the tangible and the online world. So, think things like textures on the main background, or maybe 3D elements that feel like you can almost touch them on the site instead of just scrolling through it. But, here's the key in all of this.

All of these textures, all of this depth needs to be subtle. We don't want to compete with the star of the show. So, think of it like real-world details that are just kind of there. You You notice them, but they're not asking for your attention. So, let's go ahead and do that with the example that we've been working on. First, let's add some texture to the star of the show.

We'll just add a little bit of noise to it. There's this really cool plugin called noise and texture that allows you to do that straight within Figma rather than having to open up Photoshop. There's just a few settings you got to select, and then bam, you're good to go. Then, I think there's an opportunity to kind of rhyme with the glass feel of the star of the show, and then add a little bit more depth to it by taking these cards and some of the elements on our navigation and just adding some glass effect. And now it's definitely starting to feel like just more than code and pixels on a floating page. Our next tip is actually even more subtle, if you can believe it, but it can make a pretty big difference.

Early on in my web design journey, I got really into reading other businesses' design systems. &gt;&gt; &gt;&gt; Kind of nerdy, I know, but helpful. And when I was reading Google's material design, I noticed something. They don't just use 100% opacity on all of their text. They literally spell out 87% opacity for text that's high emphasis, or the important stuff, and then 60% for the medium emphasis. There's a little bit of debate about why they do this, but regardless of where you land, using opacity is a massive win for hierarchy.

Your eye immediately knows what to read first, what you can skim through, and then maybe what to ignore unless you really need it. And you can steal that exact idea on your own website. Now, let's keep this headline at 100% opacity. This is actually what we want people to pay attention to the most when they first visit our website. But, we can take this subheading and drop that puppy all the way down to 70%. And here's a little bit of the before and after.

The one on top, 100% opacity on all the text. The one on the bottom has a few levels. Like I mentioned before, it's pretty subtle, but man, it really makes this page feel intentional. This final tip is one that most web designers aren't going to do, but it's going to make a huge difference in the outcome of the websites that you're working on. I got this idea from a concept that I learned when I was doing music for a living and I was producing people's albums and I learned that the best producers will hear an artist's song and then have them speed it up a lot and then slow it way down a lot. Maybe sing the octave up or sing the octave down.

Maybe change the keys. Doing that forces the musicians out of their original thoughts so that they can finally find something that is the absolute best version of the song. But you can't do that if you're just taking the first version and then trying to adjust it until it's better and better. You got to just do something completely different. The same is true with web design. Take your first thought and then try something totally different.

Maybe make a light mode. Maybe change the layout. Try a different star of the show. This one example that I showed you throughout the video had 12 different versions of the same star. The first version would have probably been fine, but if I hadn't kept going, it wouldn't have been nearly as good. So play around.

Have fun with your ideas until that angel gets carved out of the rock like Michelangelo used to say. These tips can instantly level up almost any website that you're working on, but they're still just that. Tips. If you want to become the kind of designer who can walk into absolutely any project and know exactly what to do, you have to move past tips and build the underlying skills. That's why I made this video. The only five web design skills that actually matter.

Check that out next and go design something great. Don't forget, if you don't quit, you win.
</transcript_1>

<transcript_2>
How To Build a Website SO Premium They Beg You To Buy
Chaîne : Sam Crawford | Web Design Expert | Durée : 12:36 | https://www.youtube.com/watch?v=7p-ZPK3GfI8

Most websites look cheap. And I don't mean they're poorly built or anything like that. What I mean is they feel cheap. And when someone lands on a cheap site, within 2 seconds, they've already made a judgment about that business. That judgment is usually not a good one. Which is why today I'm going to break down exactly what makes a website feel premium versus what makes it look like you just built it yourself on a Friday night.

After working with multiple Fortune 500 companies and generate a north of $10 million in incremental revenue, I've noticed there are specific things that separate the websites people want to buy from and the ones they want to leave immediately. By the end of this video, you'll understand what actually makes a site feel expensive. You'll be able to spot it when you see it, and you'll also know exactly what to look for when building your own site. Okay, so let's start with the reality of where most websites are right now. I see two main situations. First, you've got people who hired a developer years ago and now they're completely locked in.

Let's say they want to change a single line of text on their homepage because they changed what, you know, whatever their service offerings are. More often than not, that'll take a support ticket, maybe two weeks of waiting, and in some cases extra money on top of an existing retainer. They have zero autonomy, and that lack of control becomes this constant frustration within the business. Then you've got the other group, people who did it themselves or hired someone cheap. And look, I do get it. Budget constraints are real.

But here's the issue. In that case, there's no actual strategy behind the site. The site map itself doesn't even make sense. The site itself isn't structured for SEO or AIO. It's not guiding people towards any real call to action. And honestly, it's not doing even a fraction of what a website could do for the business.

If I had to rate it on a scale of 0 to 10, most sites I see are probably sitting around a two. And the reason why is because when someone lands on it, their immediate thought is these people don't look professional. And that perception, it sticks. So that is the exact problem that we're going to solve today in this video. So here's the number one thing that makes a website feel premium. It's bespoke assets.

And I know that sounds kind of vague. So let me explain what I mean. Most cheap websites are just text. You've got text that sits on a plain background and then maybe you've got some stock photos thrown in. But when you add custom graphics, and I mean actually custom, like not generic icons from some free library, something shifts. Suddenly, you've got depth, you've got visual interest, and the site starts to feel intentional.

What we'll do for clients is we'll create these custom graphics specifically for the client. They're not just decorative. What they do is they serve a purpose. They break up content and they guide the eye. And what it does is it makes information easier to digest for the visitor. But here's the thing that separates something that's premium from something that looks quite amateur.

The graphics themselves have to feel like they belong. So what they have to do is match the brand, the tone of the business, and then the overall aesthetic of the site. Because if you've got a graphic that looks out of place, it's much worse than having no graphic at all. When it's done right, though, it completely changes how a site feels. It's the difference between someone just clicking around your site and leaving and someone actually stopping to read what you have to say. Okay, so this next one's huge and I think a lot of people underestimate how much it matters and that's brand guidelines.

Specifically, your logo, your color palette, and your fonts. So, let's start with the logo. A professional logo doesn't have to be complicated, but it does have to be intentional. It has to look like someone who knows what they're doing created it. If your logo looks like it was made in Canva in 15 minutes, then people are going to viscerally feel it. Next is your color palette.

And this is where I see so many people mess up. What they'll do is they'll pick like five colors that they think work individually, but they don't work together. There's no cohesion whatsoever. And a premium color palette is cohesive. The colors complement each other and they work together to create a mood and a feeling and a brand identity throughout the site. So when someone's scrolling through your site, the colors should feel intentional and not random.

But the biggest one is fonts. Fonts can completely change how a site looks. If you think about like a a childish font, an outdated font, or a font that's hard to read, even any of those will instantly make your site feel cheap. But the right fonts will make your site feel sophisticated and often times more sophisticated than your brand even is. So when you pay attention to all these things, what it does is it makes people feel like you care about the details. And that's what premium is.

It's all in the details. You combine a professional logo, a cohesive color palette, and then thoughtfully chosen fonts. You'll have the foundation for a premium site. Everything else builds on top of that foundation. So, here's something that separates good sites from great sites. I'm talking about subtle animation, not the kind where you've got everything kind of bouncing around and spinning and distracting a visitor from what they're actually reading.

That's the opposite of premium. It's cool for a moment, but in reality, people see all these wacky animations and they're just overwhelmed. So, what I mean by subtle animation is when someone scrolls down your page, you've got nice elements that fade in. When a visitor hovers over a button, it responds in kind. When they land on a new section, things move in a way that feels natural and it guides their attention to where you want them to go. It's like the difference between a website that feels sort of dead and static versus one that feels alive.

The animations that we use are designed to reduce what we call rage clicks. You know, when someone's so confused or overwhelmed on your site that they just start sort of clicking everywhere trying to see what is responsive. We want to prevent that. We want to guide people through the site smoothly. Obviously, keep them engaged and make sure they're not overwhelmed because when you do it right, animation is a great way to do that. It's subtle enough that people don't consciously notice it, but they do feel it.

And that feeling is what separates a site that people want to spend time on versus one that they want to leave. All right, so we've covered the visual stuff, the graphics, the branding, the animations, but here's what I'm realizing. A lot of people know what makes a site look premium, but they don't know how to actually build it or they know what they want, but they don't know how to communicate it to a designer. So, what I've done is I've put together a free guide called the premium website checklist. It's literally a checklist of every element we've talked about today, plus about 15 or so other things that separate premium from cheap. So, what you can do is you can use it to audit your own site or if you're hiring someone, you can use it to make sure they're actually building something premium for your business.

What I'll do is I'll drop the link in the description. It's completely free. Just grab it and start using it. Anyway, let's keep going. So, we've talked about the visual stuff, but here's where a lot of otherwise very premium sites actually fall apart, and that's the structure. And I'm talking about the actual architecture of the site, the site map itself, the way pages flow into each other, how information is organized.

A cheap site has pages that might make sense individually, but together they don't make any sense. So someone lands on your homepage and the next logical step isn't clear. Do they go to your services page? If you've got multiple services, which page do they go to? Do they go to your about page, your contact page? They're confused.

And this confusion will always lead to an action. A premium site on the other hand guides people. Every page has a purpose. Every page leads somewhere. And there's a clear journey from landing on the site to taking action. And that action, which is your call to action, has to be crystal clear.

You don't want it just buried in the footer. It's got to be obvious. It's got to be easy to find. And most importantly, it's got to be easy to take. But not only is this important from a purely conversion perspective, this is where SEO comes into. A premium site isn't just visually impressive or congruent or properly copywritten.

It's structured in a way that search engines understand. And it's also organized in a way that makes sense for both people and algorithms. So your site map, your page hierarchy, your internal linking, all of that matters. These are the parts I know that they're just not flashy. They're not sexy and they're typically not something that people will consciously notice. But things like the site map, UX, and your CTAs are the difference between a site that actually sees insane return on investment and brings in so much business versus one that just sits there and looks nice.

Now, I want to take a moment to speak directly about what we do to make premium websites, which I want you to know whether you end up working with us or not. Because here's what really separates what we do from what a lot of other designers and developers may do. After we build a site, the client actually owns it. And more than that, they can actually update it. They can make changes. They can add new content without waiting for us, without paying extra, without feeling like they're locked into a one-way contract.

And listen, I know that sounds like it should be standard, but it's it's not. A lot of developers will build sites that are basically, you know, black box. You can't touch them. You need a developer to do everything and anything on the site. That's not premium. That's a trap.

And quite frankly, it's a business model that gives the web design industry quite a bad name. Then on the other hand, a premium site would actually empower the client. This is what we do. It's built in a way that's intuitive. It's easy to update. The client feels like they own it because they do.

And here's why this matters for the overall feel of the site. Because when a client can easily update their site, they do. They keep content fresh. They add new case studies. They update their services. And the site stays alive.

It stays relevant. And that freshness, that aliveness, that's something people feel when they land on a site. It's the difference between a site that feels current and professional versus one that just feels abandoned. So, when we're building a premium site, we're not just trying to make it look good. We're making it something that the client can actually use and maintain. And that's the transformation that we offer.

And on that note, I want to mention what proper handover and post-launch care looks like. So, as an example, we've built this premium site. It looks amazing, and it's structured perfectly. The client sat there ready to launch. But here's where a lot of people mess up. They just kind of hand it over and disappear.

Again, that's not a premium service. What that is is it's cutting and running. Not only is it bad for the client results, obviously, but it's just bad business on behalf of the agency or the freelancer building the site. So, here's what we do instead. We'll sit there and we will record a full handover training session for the client. If they want a live training session, we will do that, too.

We'll walk the client through the site, show them exactly how to update it, how to add new content, how to use all the features that we've built for them. Then what we'll do is we set clear expectations about what they can do dayto-day and what they might need a little bit of help with in the future. And then for the first 30 days post launch, we're available for free email support. So any questions, any issues, anything they're not sure about, the team are there. Or our goal is with this is to make sure nothing goes wrong. And if they do want ongoing support after that, we have like a a hosting and maintenance plan that we offer.

So, we're on hand with 2 hours of team time per month to make changes, plus 24/7 access to our concierge team for any questions. It's not really that expensive, but what it means is clients who don't always want to be on the site all the time have that flexibility of having a team on hand whenever they need it. And that is what premium service looks like. It's not just about the product. It's about the entire experience from that first call to months after launch. We're showing that we care and clients can feel that.

Now, if you want to see what Premium looks like in action, I've got a whole portfolio of sites that we've built and I'll link to that in the description. If while you're checking out our work, something catches your eye and you decide you want your own custom website to look just like that, you can book in a call and speak to the team. That said, if you only want to just keep watching, that's okay, too. If you click here, you can check out the next video where I'll walk you through an entire before and after of a website that we designed for an energy company. So you can see exactly what our work looks like in real time and get an idea for how we could transform your site.
</transcript_2>
````
