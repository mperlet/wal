# ![Alt text](static/img/whale_fav.png "Write a Letter") wal - Write A Letter

Webapp to create a Din-A4-Letter online with LaTeX.

### Logo & Name
The logo is a whale, the german word for whale is *Wal*.
Wal stands for Write-A-Letter. ;-)


## Installation with Vagrant

```
git clone https://github.com/mperlet/wal.git && cd wal
vagrant up
```
By default, wal runs on port 5000. Check `http://localhost:5000`.

## Installation with Docker

```
docker build -t wal .
docker run -p127.0.0.1:5000:5000 -d -t wal
```

## Try it

[wal.mperlet.de](http://wal.mperlet.de/ "Write A Letter")

## Contributing
1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## Credits

* [Flask](http://flask.pocoo.org/)
* [Bootstrap Readable](http://bootswatch.com/readable/)
* [Whale Logo](http://pixabay.com/de/blau-skizze-silhouette-cartoon-36713/)
* [LaTeX](http://www.latex-project.org/)

## License
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
